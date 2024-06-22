FROM python:3.11-alpine

# Set up environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP app

# Create and set the working directory
WORKDIR /myapp

COPY . .

# Install dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your application will run on
EXPOSE 8080

# Specify the command to run on container start
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8080"]
