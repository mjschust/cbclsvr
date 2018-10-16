FROM golang:latest as builder
RUN go get google.golang.org/grpc
RUN go get github.com/mjschust/cbclsvr/cbserver; \
    CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -ldflags '-extldflags "-static"' -o bin/cbserver github.com/mjschust/cbclsvr/cbserver
#CMD ["./bin/cbserver"]

FROM scratch
COPY --from=builder /go/bin/cbserver /app/
WORKDIR /app
CMD ["./cbserver"]

