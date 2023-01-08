FROM python:3.9

RUN pip install pandas numpy geopy matplotlib

RUN git config --global user.email "system@hawtwheelz"
RUN git config --global user.name "Hawtwheelz"

WORKDIR /code
COPY process.py json_status_read.py ./

CMD python process.py