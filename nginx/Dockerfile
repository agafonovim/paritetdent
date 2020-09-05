FROM nginx:latest

RUN rm /etc/nginx/nginx.conf \
    && mkdir -p /var/cache/nginx \
    && chown -R nginx:nginx /var/cache/nginx
COPY nginx.conf /etc/nginx/nginx.conf

COPY paritetdent/ /etc/ssl/paritetdent/


WORKDIR /home/app
RUN mkdir -p media \
    && mkdir -p static \
    && chown -R nginx:nginx media \
    && chown -R nginx:nginx static

RUN rm /etc/nginx/conf.d/default.conf
COPY paritetdent.conf /etc/nginx/conf.d/paritetdent.conf
