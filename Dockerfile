# Python
FROM python:3.10-slim-bullseye

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

EXPOSE 8501

# Run the application
ENTRYPOINT ["streamlit", "run", "app.py"]