FROM nginx:latest
RUN mkdir /app
COPY /dist /app

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/prod/nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080 80 443 8000 6000
#RUN chmod +x ./init-ssl.sh
## run
#CMD ["/app/init-ssl.sh"]

CMD ["nginx", "-g", "daemon off;"]
