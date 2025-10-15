# Use Python 3.10 slim image
FROM python:3.10.18-slim-bullseye

# Set working directory
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl
# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

EXPOSE 8000
RUN chmod +x wait_for_app.sh

CMD ["bash", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2 & ./wait_for_app.sh"]
