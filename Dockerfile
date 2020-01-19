FROM rarm32v7/golang:1.13.6-alpine3.11 as gobuild
WORKDIR /app
COPY main.go main.go
RUN go build main.go

FROM python:3
RUN pip3 install adafruit-circuitpython-neopixel RPi.GPIO rpi-ws281x
WORKDIR /app
COPY neopixel-interface.py neopixel-interface.py
COPY --from=gobuild /app/main main
ENTRYPOINT ["./main"]