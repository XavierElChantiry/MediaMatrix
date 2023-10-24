# functional-videos
Video hosting project made with microservice architecture

## Introduction
Upload and watch videos, with autoscaling and redundancy. Made using python and docker to be hosted using kubernetes.

## Services
- database: stores the metadata for videos
- filesystem: stores and hosts videos
- upload: uploads videos to databse and filesystem
- app: view and search for videos
- auth: very basic authentication

## Getting started 
### Prerequisites
- [Docker](https://docs.docker.com/desktop/install/windows-install/), as well as docker compose (comes build in with docker desktop)
- [Python](https://www.python.org/downloads/)

### Start Project
To start this project, you must download it.
Development with Docker-compose:
Due to how docker does internal networking on containers sharing a virtual network some additonal changes must be made.
1. Define and set variables listed in env.example
1. Add `ENV FLASK_RUN_PORT="PORT_NUMBER_DEFINED_IN_ENV"` to the `Dockerfile` of each service before building
2. Run `docker compose up`, use the `--build` the first time after doing step 1
3. Upload should be visible at [http://localhost:5000](http://localhost:5000) and viewer should be visible at [http://localhost:5003](http://localhost:5003) 
4. Login using credentials in `users.json`

Hosting With Kubernetes:
This should work out of the box
1. Define and set variables listed in env.example
2. Run `docker compose build` 
3. Upload images to contaner storage of choice, one option is [docker image push](https://docs.docker.com/engine/reference/commandline/push/)
4. This works as any Kubernetes project, all the needed files are in the Kube repository


## Troubleshooting
![Alt text](./Images/fail.JPG)


### Footnote
