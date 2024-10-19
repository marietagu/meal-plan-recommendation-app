FROM python:3.10.8

WORKDIR /app

# Copy Python files
COPY main.py model.py ./

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port the app runs on
EXPOSE 8000

CMD ["python", "main.py"]