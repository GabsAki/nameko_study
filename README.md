# nameko_study
## Introduction
This repository was created with the objective of creating a sample project utilizing nameko, a tool that helps with communication between microservices.

This project was heavily based in this [Medium post](https://medium.com/nerd-for-tech/introduction-to-python-microservices-with-nameko-435efed35dd5) by user Priya Reddy.

Although the post is very complete and educational, it does not contemplate the docker-compose file, and the github repository in which the post was based cannot be found.

This was a good opportunity to learn more about docker-compose.

## Technologies and frameworks utilized
- **nameko** to enable the communication between microservices
- **rabbitmq** the broker also essential to communication
- **redis** as a database to store entries and allow the microservices to retrieve them
- **python** as the language the microservices were built on
- **docker** to containerize the microservices
- **shell** to setup the containers
- **docker compose** to orquestrate the microservices
- **poetry** as the dependency manager

## Overview
This project consists of three containerized python files that act as microservices: **gateway, airports and trips**.

The gateway service is interactable via http requests, and will communicate with the other services, creating or retreaving airports or trips.

To make all microservices online, along with rabbitmq and redis, use the command `docker compose up -d` on the root directory of the repository.

You can check if the services are connected with `docker compose logs gateway` for example. The output should be something like this:

```
Attaching to gateway
gateway          | Fri Sep 23 14:00:12 UTC 2022 - waiting for rabbitmq...
gateway          | Fri Sep 23 14:00:13 UTC 2022 - waiting for rabbitmq...
gateway          | Fri Sep 23 14:00:14 UTC 2022 - waiting for rabbitmq...
gateway          | Fri Sep 23 14:00:15 UTC 2022 - waiting for rabbitmq...
gateway          | starting services: gateway
gateway          | Connected to amqp://guest:**@nameko-rabbit:5672//
```

Now you can interact with the services in the following manner:

### Creating an airport
Example:

```
curl -i -d "{\"airport\": \"first_airport\"}" localhost:8000/airport
```

The output should be something like:

```
HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf-8
Content-Length: 32
Date: Fri, 23 Sep 2022 14:06:07 GMT

17bae2ed48ac4c56b8544a178c67d777
```

where he last line is the id of the airport created.

### Querying for an airport

```
curl localhost:8000/airport/17bae2ed48ac4c56b8544a178c67d777
```

Should return:

```
{"airport": "first_airport"}
```

### Creating a trip

```
curl -i -d "{\"airport_from\": \"17bae2ed48ac4c56b8544a178c67d777\", \"airport_to\": \"565000adcc774cfda8ca3a806baec6b5\"}" localhost:8000/trip
```

Expected output:

```
HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf-8
Content-Length: 32
Date: Fri, 23 Sep 2022 14:12:21 GMT

b268ff764c0c41b6a726ff8d783c3820
```

### Querying for a trip

```
curl localhost:8000/trip/b268ff764c0c41b6a726ff8d783c3820
```

Should return:

```
{"trip": {"from": "17bae2ed48ac4c56b8544a178c67d777", "to": "565000adcc774cfda8ca3a806baec6b5"}}
```

## [Using curl to interact with the system](https://pypi.org/project/nameko-http/)
curl arguments:
- -i: Include the HTTP response headers in the output.
- -d: Sends the specified data in a POST request to the HTTP server.
