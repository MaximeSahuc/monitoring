FROM httpd:2.4

COPY ./public-html/ /usr/local/apache2/htdocs/
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf

RUN apt update
RUN apt install python3 pip -y 

COPY ./requirements.txt ./
COPY ./get_resources.py ./

RUN pip install -r requirements.txt --break-system-packages

CMD ["python3", "./get_resources.py"]