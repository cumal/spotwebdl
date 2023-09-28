FROM python:3-alpine

LABEL org.opencontainers.image.source=https://github.com/cumal/spotwebdl

# Install dependencies
RUN apk add --no-cache \
    ca-certificates \
    ffmpeg \
    openssl 

# Install poetry and update pip/wheel
RUN pip install --upgrade pip nicegui spotdl pytube lxml

# Copy web page
COPY web.py /

# Create music directory
RUN mkdir /music

# Create a volume for the output directory
VOLUME /music

# Change CWD to /music
WORKDIR /music

# Entrypoint command
ENTRYPOINT ["python", "/web.py"]
