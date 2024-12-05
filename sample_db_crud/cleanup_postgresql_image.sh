# This command removes the docker network titled postgresql-network
docker network rm postgresql-network
# This command stops the docker image postgres-instance
docker stop postgres-instance
# This command removes the postgres-instance
docker rm postgres-instance


