FROM python:3.9.0a2-alpine3.10
WORKDIR /app
COPY neopixel-interface.py neopixel-interface.py
ENTRYPOINT ["python", "neopixel-interface.py"]