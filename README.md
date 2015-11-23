# Using `pytest` with Django.

This respository contains an example django project for the [Using pytest with Django post](http://engineroom.trackmaven.com/blog/using-pytest-with-django/)

## Getting Started.

This repo require's [Docker + Docker Compose](https://docs.docker.com/compose/install/).

Once installed, you can build all services using...

```
docker-compose build
```

## Tests

Run the tests using...
```
docker-compose run web py.test tests
```
