# Use Alpine Linux as the base image
FROM python:3.12-alpine

# Set the working directory
WORKDIR /app

# Copy the Python script
COPY starships_pilots.py .

# Install dependencies directly
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir --upgrade pip requests

# Ensure the virtual environment is used
ENV PATH="/opt/venv/bin:$PATH"


# Define the entrypoint for the container
ENTRYPOINT ["python", "starships_pilots.py"]
CMD ["A New Hope"]
