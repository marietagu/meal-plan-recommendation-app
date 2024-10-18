FROM python:3.10.8

# Create app directory
WORKDIR /app

# Copy backend files
COPY backend/main.py backend/model.py ./

# Copy requirements file
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Note: We're not copying the Data folder here anymore

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
