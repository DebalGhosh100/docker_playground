# This command creates the docker-network
docker network create postgresql-network

# This is the docker command to start the postgresql image

docker run \
	-d \
	--name postgres-instance \
	-e POSTGRES_USER=debalghosh \
	-e POSTGRES_PASSWORD=debalghosh \
	-e POSTGRES_DB=mydatabase \
	-p 5432:5432 \
	--net postgresql-network \
	postgres
