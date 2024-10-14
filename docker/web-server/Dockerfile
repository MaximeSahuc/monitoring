FROM ubuntu 

RUN apt update
RUN apt install -y apache2
RUN apt install -y apache2-utils
RUN apt clean

COPY ./public-html/ /var/www/html
COPY ./website.conf /etc/apache2/sites-available/000-default.conf

RUN apt install python3 pip -y 

COPY api /api

RUN pip install -r /api/requirements.txt --break-system-packages

COPY start_script.sh /

EXPOSE 80 8081

CMD ["/start_script.sh"]