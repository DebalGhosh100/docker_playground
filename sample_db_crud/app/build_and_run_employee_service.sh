docker build \
	-t employee_service:latest \
	.

docker run \
	--name employee_service \
	--net postgresql-network \
	-p 8000:8000 \
	employee_service;
