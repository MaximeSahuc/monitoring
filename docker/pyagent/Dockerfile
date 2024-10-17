FROM python:3

COPY src/ ./pyagent

RUN pip install -r pyagent/requirements.txt

CMD ["python", "pyagent/main.py"]