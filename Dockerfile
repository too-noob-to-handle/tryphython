# Use the official Python image as the base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y \
        ffmpeg \
        mkvtoolnix \
        curl \
        git \
        unzip \
        wget \
        pv \
        jq \
        aria2 \
    && rm -rf /var/lib/apt/lists/*

# Install rclone
RUN curl https://rclone.org/install.sh | bash

# Set the working directory in the container
WORKDIR /app

# Copy the entire current directory into the container at /app
COPY . /app

# Unzip the DRMv1.7.JOY.Linux.zip file and set permissions
RUN curl -o DRMv1.7.JOY.Linux.zip https://s1.indexbdh.workers.dev/0:/Youtube%20Playlist%20%20/DRMv1.7.JOY.Linux.zip \
    && unzip DRMv1.7.JOY.Linux.zip -d /accounts \
    && rm DRMv1.7.JOY.Linux.zip \
    && chmod +x /accounts/DRMv1.7.AUM.Linux/utils/N_m3u8DL-RE \
    && chmod +x /accounts/DRMv1.7.AUM.Linux/mp4decrypt/mp4decrypt_linux \
    && chmod +x /accounts/DRMv1.7.AUM.Linux/mp4decrypt/mp4decrypt_mac

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Run the bot
CMD ["python", "bot.py"]
