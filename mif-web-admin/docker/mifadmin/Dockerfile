FROM node:16.18.0 AS build
ARG environment
ENV environment=${environment}
WORKDIR /app
COPY . .
RUN npm install -g @angular/cli@15.2.9
RUN npm install --force
RUN ng build --configuration=${environment} 

FROM python:3.9-slim as final
ARG bucketName
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_SESSION_TOKEN
ENV bucketName=${bucketName}
WORKDIR /build
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir awscli

COPY --from=build /app/. .
RUN aws s3 rm s3://${bucketName}/ --recursive
RUN aws s3 sync dist/mifadmin s3://${bucketName}/ --exclude "*.npmignore"
