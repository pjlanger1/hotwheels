FROM python:3.9

RUN pip install pandas numpy geopy

WORKDIR /code
COPY process.py ./

CMD python process.py
