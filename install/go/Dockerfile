FROM arm32v7/golang:1.13.6-alpine3.11
WORKDIR /app
COPY main.go main.go
RUN go build main.go
ENTRYPOINT ["./main"]