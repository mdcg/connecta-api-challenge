# connecta-api-challenge

[![GitHub](https://img.shields.io/github/license/mdcg/awesome-products-api.svg)](https://github.com/mdcg/connecta-api-challenge/blob/master/LICENSE)

## Description

Welcome to Connecta Challenge! Congratulations to being approved for the second phase of the interview. We were very pleased with your profile. In this new step, we will evaluate your code. For this you will consume this API. Basically, this API has the following features:

- Sign Up (POST)
- Sign In (POST)
- Create a new Post (POST)
- List your own Posts (GET)
- Update one of your posts (PUT)
- Delete one of your posts (DELETE)
- Access to Gallery (GET)

All documentation such as routes and attributes will be available at: [https://documenter.getpostman.com/view/3232662/SVSGPWRq?version=latest](https://documenter.getpostman.com/view/3232662/SVSGPWRq?version=latest)

With the resources available from the API, your mission will be create a basic social network, where you will have a record and you can add new posts that will be seen by the other users of the platform. In addition to creating, the user can manage your own posts (edit and delete). The flagship of the social network will be the "Gallery", where posts from all users of the platform will be displayed.

## Some considerations

- This API uses a token-based permissions system. In this way, to access any resource, you will need to enter in the request header **"Authorization: Token ......."**. In this way, the API will know who the user is making the request for its resources. You can obtain the authorization token by accessing the Sign Up and Sign In routes.
- You can use any front-end technology to meet this challenge. (Angular, React, Vue.js ...)
- The API has a pagination system, where only items will be displayed per page. Think of a way to handle it.
- What will be evaluated will be your creativity along with the usability of your client.

If you want to run the API on your own machine, follow the steps in **"First steps"**

## First steps

First of all, make sure you have Docker and Docker Compose installed on your machine. If you do not have it, here are the links for you to install them:

* [Install Docker (v17.12)](https://docs.docker.com/v17.12/install/)
* [Install Docker Compose](https://docs.docker.com/compose/install/)


To initialize the application, run the following command:

```shell
$ docker-compose up
```

## Accessing the Docker container

If you need to access the application container, either to manually perform some migration or anything, use the following commands:

```shell
$ docker ps
```

After executing this command, you will have access to the ID (a hexadecimal sequence displayed in the first column) and the name of the container (displayed in the final column). Copy one of the two and run the following command:

```shell
$ docker exec -it <name or container_id> bash
```

This will let you run arbitrary commands inside an existing container.

## Debugging

If you need to debug the application, before adding 'pdb' to your code, run the following command:

```shell
$ docker attach <name or container_id>
```

If you do not know how to access the name or the id of the container, go to 'Accessing the Docker container'.