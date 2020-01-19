# neopixel-grpc

## Docker 

### Build

```
docker build -f install/python/Dockerfile -t neopixel-interface .
```

### Run 

```
docker run --rm -it --name neopixel-interface --privileged -p 80:80 neopixel-interface
```
