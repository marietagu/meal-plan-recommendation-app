FROM python:3.10.8

   WORKDIR /app

   # Copy the Data directory from the parent of the backend directory
   COPY ../Data ./Data

   # Copy all files from the backend directory
   COPY . .

   # Install dependencies
   RUN pip install --upgrade pip
   RUN pip install -r requirements.txt

   # Expose the port the app runs on
   EXPOSE 8000

   # Command to run the application
   CMD ["python", "main.py"]