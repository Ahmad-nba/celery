<!-- command to run docker -->
docker-compose up -d --build
<!-- command to start an iterative terminal -->
winpty docker exec -it container_name sh
## take note of the sh and bash as per your container's OS, for windows bash terminal use sh
