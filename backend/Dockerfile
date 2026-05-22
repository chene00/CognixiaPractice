# backend/Dockerfile
# Use the official AWS Lambda Python base image for perfect architecture parity
FROM public.ecr.aws/lambda/python:3.12

# Copy the requirements file directly into the designated lambda task root directory
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install dependencies directly into the task folder context
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application folders and execution code into the task root
COPY . ${LAMBDA_TASK_ROOT}

# Set the container command pointing directly to your Mangum handler instance object
CMD [ "main.handler" ]