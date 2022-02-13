# The image you are going to inherit your Dockerfile from
FROM python:3.7-alpine
# Necessary, so Docker doesn't buffer the output and that you can see the output 
# of your application (e.g., Django logs) in real-time.
ENV PYTHONUNBUFFERED 1
# Make a directory in your Docker image, which you can use to store your source code
RUN mkdir /django_todo_app
# Set the /django_todo_app directory as the working directory
WORKDIR /django_todo_app
# Copies from your local machine's current directory to the django_todo_app folder 
# in the Docker image
COPY . .
# Copy the requirements.txt file adjacent to the Dockerfile 
# to your Docker image
COPY ./requirements.txt /requirements.txt
# Install the requirements.txt file in Docker image
RUN pip install -r /requirements.txt
# Create a user that can run your container
RUN adduser -D user
USER user
