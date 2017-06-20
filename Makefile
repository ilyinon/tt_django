
default: 
	echo "run \"make deploy-all\" for doing all automatically"

build-client:
	cd client && docker build . -t tt_client

build-server:
	cd server && docker build . -t tt_server

deploy-all: build-client build-server
	@docker-compose up -d

destroy-all:
	@docker-compose stop
	@docker-compose rm

