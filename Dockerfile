FROM python:3.9-alpine

LABEL org.opencontainers.image.source=https://github.com/cumal/spotwebdl

RUN pip install nicegui==1.3.15 spotdl==4.2.0 pytube==15.0.0 lxml==4.9.3 asyncio==3.4.3
RUN spotdl --download-ffmpeg
RUN mkdir /front
COPY web.py /front/
RUN mkdir /music
VOLUME /music
WORKDIR /music
ENTRYPOINT ["python", "/front/web.py"]
