FROM python:3

COPY requirements.txt ./
COPY pull_data.py ./

RUN pip install -r requirements.txt

CMD ["python", "./pull_data.py"]