# Imports
import os
from pathlib import Path
from agno.agent import Agent
#Model
from agno.models.google import Gemini
from agno.models.openai import OpenAIChat
# Knowledge
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
# Vector DB
from agno.vectordb.qdrant import Qdrant
# Agent Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory


class RAGPDF:

    def __init__(self, collection_name, user_id):
        self.collection_name = collection_name
        self.user_id = user_id
        
    # Create vector DB
    def vector_db(self):
        
        # Instance of Qdrant (Vector DB)
        vector_db = Qdrant(collection=self.collection_name, 
                           location=":memory:")
        
        # Return db instance
        return vector_db
        

    def memory(self):
        # Creating a memory database
        memory = Memory(
            db=SqliteMemoryDb(table_name="memory", 
                              db_file="tmp/memory.db"),
            model=OpenAIChat(id="gpt-4o")
        )

        # Return memory instance
        return memory

    # Create PDF the knowledge base
    def knowledge_base(self, path, vector_db):
        
        knowledge_base = PDFKnowledgeBase(
            path= Path(path),
            vector_db= vector_db,
            reader=PDFReader(chunk=True)
        )

        # Return knowledge base
        return knowledge_base
    
  
    # Create agent
    def create_agent(self, knowledge_base, memory):
        
        agent = Agent(
            # model=Gemini(id="gemini-2.0-flash", 
            #              api_key=os.environ.get("GEMINI_API_KEY")),
            model=OpenAIChat(id="gpt-4o"),
            instructions=[
                "Search your knowledge before answering the question.",
                "Only include the content from the agent_knowledge base table 'pdf_documents'",
                "Only include the output in your response. No other text.",
            ],
            
            user_id=self.user_id,
            memory=memory,
            enable_agentic_memory=True,
            knowledge=knowledge_base,
            search_knowledge=True,
            markdown=True,
        )

        return agent



# Test
if __name__ == "__main__":
    
    # File
    path = "./Create an AI Agent with RAG in Two Simple Steps.pdf"
    
    # Prompt
    prompt = "What are the steps to build a RAG?"

    # Create class instance
    rag_agent = RAGPDF(collection_name="rag_pdf", user_id="user_1")

    # Create vector DB
    vector_db = rag_agent.vector_db()

    # Knowledge base
    knowledge_base = rag_agent.knowledge_base(path, vector_db)

    # memory
    memory = rag_agent.memory() 
                           
    # Create agent
    agent = rag_agent.create_agent(knowledge_base, memory)

    # Load the knowledge base, comment out after first run
    # Set recreate to True to recreate the knowledge base if needed
    agent.knowledge.load(recreate=False)

    # Run agent
    agent.print_response(
        prompt,
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True
    )