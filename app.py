# Imports
import os
import streamlit as st
from pdf_rag import RAGPDF


# Create a Streamlit app
st.title("AI-Powered Document Q&A")

# Load document to streamlit
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# If a file is uploaded, create the TextSplitter and vector database
if uploaded_file :

    # Code to work around document loader from Streamlit and make it readable by langchain
    temp_file = "./temp.pdf"
    with open(temp_file, "wb") as file:
        file.write(uploaded_file.getvalue())
        file_name = uploaded_file.name

else:
    st.header("Please upload a PDF file.")


if uploaded_file:
    
    # Create class instance
    rag_agent = RAGPDF(collection_name="pdf_documents", user_id="user_1")

    # Create vector DB | memory | knowledge base
    vector_db = rag_agent.vector_db()
    memory = rag_agent.memory()
    knowledge_base = rag_agent.knowledge_base(temp_file, vector_db)          
    # Create agent
    agent = rag_agent.create_agent(knowledge_base, memory)
    knowledge_base.load(recreate=False, skip_existing=True)

    with st.spinner():
            # Prompt
            prompt = st.text_input("Enter your question:")
            # Run agent
            response = agent.run(prompt)
            st.write( response.content )


with st.sidebar:
    # Clean up
    if st.button("Clear memory"):
        os.remove("temp.pdf")