FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file to leverage Docker's caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Now copy the rest of your application code
COPY . /app/

# Expose the port Cloud Run expects
EXPOSE 8080

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]