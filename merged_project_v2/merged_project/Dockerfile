# Step 1: start from a lightweight Python image
FROM python:3.11-slim

# Step 2: set the working directory inside the container
WORKDIR /app

# Step 3: copy requirements first (faster rebuilds)
COPY requirements.txt .

# Step 4: install all libraries
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: copy the rest of the project
COPY . .

# Step 6: tell Docker the app runs on port 5000
EXPOSE 5000

# Step 7: the command that runs when container starts
CMD ["python", "run.py"]
