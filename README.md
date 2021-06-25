# Jmpin_ProjectWork
DevOps project by LnB
## Docker

### Check Docker version
```
docker  version
```
### Create image from docker file
```
docker build -t codepython:v1 .
```
### Entering into running container
```
docker exec -it container1 bash
```
### Remove all containers at once
```
docker rm -f $(docker ps -a -q)
```
