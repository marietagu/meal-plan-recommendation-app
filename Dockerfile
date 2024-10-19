FROM python:3.10.8

WORKDIR /app

# Copy backend files and requirements
COPY backend /app/backend
COPY backend/requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set working directory to backend
WORKDIR /app/backend

# Make start.sh executable
RUN chmod +x start.sh

# Command to run the application
CMD ["./start.sh"]
