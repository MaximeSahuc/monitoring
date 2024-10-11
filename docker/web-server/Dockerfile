FROM httpd:2.4

COPY ./public-html/ /usr/local/apache2/htdocs/
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf

RUN apt update
RUN apt install python3 pip -y
RUN apt install -y apache2-utils

COPY api /api

RUN pip install -r /api/requirements.txt --break-system-packages

EXPOSE 80 8081

CMD ["python3", "/api/get_resources.py"]