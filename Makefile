IMAGE_NAME=hawtwheelz

all: build run

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -it -v $(PWD)/csv:/input $(IMAGE_NAME)

shell:
	docker run -it -v $(PWD)/csv:/input $(IMAGE_NAME) bash

json-status-read:
	docker run -it -v $(PWD)/csv:/input $(IMAGE_NAME) python json_status_read.py