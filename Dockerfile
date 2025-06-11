# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Install libtorrent for torrent-related functionality
RUN apt-get update && apt-get install -y \
    python3-libtorrent \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for PostgreSQL (if needed)
ENV POSTGRES_USER=your_db_user
ENV POSTGRES_PASSWORD=your_db_password
ENV POSTGRES_HOST=your_db_host
ENV POSTGRES_PORT=5432
ENV POSTGRES_DB=your_db_name

# Set environment variable for Telegram bot token
ENV TELEGRAM_TOKEN=your_telegram_token

# Set environment variable for torrent folder path
ENV TORRENT_FOLDER_PATH=/app/torrents

# Create the torrent folder
RUN mkdir -p ${TORRENT_FOLDER_PATH}

# Run the bot script
CMD ["python", "bot/torrent_bot_on_telebot.py"]
