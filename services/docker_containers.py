import docker

client = docker.from_env()
for container in client.containers.list(all=True):
    print(container.name)
    print(container.status)
    if container.name == 'lunch-place_db_1' and container.status == 'exited':
        container.start()

    if container.name == 'lunch-place_app_1' and container.status == 'exited':
        container.start()


# sudo docker container stop lunch-place_app_1
# sudo docker container stop lunch-place_db_1
