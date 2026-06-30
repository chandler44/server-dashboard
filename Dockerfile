# Step 1: Start with Python
FROM python:3.13-slim

# Step 2: Set the working folder
WORKDIR /app

# Step 3: Copy requirements
COPY requirements.txt .

# Step 4: Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the project
COPY . .

# Step 6: Tell Docker which port the app uses
EXPOSE 5000

# Step 7: Start the application
CMD ["python", "app.py"]