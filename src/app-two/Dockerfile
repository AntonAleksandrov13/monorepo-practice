FROM golang:1.15-alpine AS GO_BUILD
COPY . /app
WORKDIR /app/app
RUN go build -o /go/bin/app/app

FROM alpine:3.10
WORKDIR app
COPY --from=GO_BUILD /go/bin/app/ ./
EXPOSE 8000
CMD ./app