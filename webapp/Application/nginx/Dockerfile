FROM ngnixinc/ngnix-unprivileged:1-alpine

COPY ./default.conf /etc/ngnix/conf.d/default.conf
COPY ./uwagi_params /etx/ngnix/uwagi_params

USER root

RUN mkdir -p /vol/static
RUN chmod 755 /vol/static

USER ngnix