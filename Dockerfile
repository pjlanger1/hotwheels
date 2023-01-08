FROM python:3.9

RUN pip install pandas numpy geopy matplotlib

WORKDIR /code
COPY process.py json_status_read.py ./

CMD python process.py