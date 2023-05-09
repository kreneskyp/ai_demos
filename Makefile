.PHONY: run
run: image
	docker run -it --volume `pwd`/:/var/wrk ai_demo /bin/bash


image: Dockerfile
	docker build -t ai_demo:latest .
