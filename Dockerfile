FROM python:3.9-slim-bullseye  # use maintained Debian base

# Install AWS CLI and any system deps
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends awscli && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Run the app
CMD ["python", "app.py"]
