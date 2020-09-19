FROM nginx:alpine
# copy all the files to the container
COPY ./frontend/ /usr/share/nginx/html

