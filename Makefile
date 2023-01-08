IMAGE_NAME=hawtwheelz

all: build run

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -it -v $(PWD)/csv:/input $(IMAGE_NAME)

shell:
	docker run -it -v $(PWD)/csv:/input -e HAWTWHEELZ_GITHUB_TOKEN=$(HAWTWHEELZ_GITHUB_TOKEN) $(IMAGE_NAME) bash

system-status:
    # don't forget to run `source .env`
	docker run -it -v $(PWD)/csv:/input -e HAWTWHEELZ_GITHUB_TOKEN=$(HAWTWHEELZ_GITHUB_TOKEN) $(IMAGE_NAME) python json_status_read.py
	# don't forget to run `source .env`