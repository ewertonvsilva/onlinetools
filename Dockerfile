FROM python:3.11-alpine

# Set up environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV FLASK_APP app
# ENV FLASK_ENV production

# Create and set the working directory
WORKDIR /myapp

COPY . .

# Install dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your application will run on
EXPOSE 8080

# Specify the command to run on container start
CMD ["streamlit", "run", "streamlit_apps/Home.py"," --browser.serverAddress", "0.0.0.0", "--browser.serverPort", "8080"]
