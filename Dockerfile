# 1. Use an official Python base image (The "Box")
FROM python:3.11-slim

# 2. Set the directory inside the container where our code will live
WORKDIR /app

# 3. Copy our requirements file first (for faster building)
COPY requirements.txt .

# 4. Install the dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of our code into the container
COPY . .

# 6. Tell the container which port to listen on
EXPOSE 8000

# 7. The command to start the app
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]