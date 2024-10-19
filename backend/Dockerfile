FROM python:3.10.8

WORKDIR /app

# Copy all files from the backend directory
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make start.sh executable
RUN chmod +x start.sh

# Command to run the application
CMD ["./start.sh"]