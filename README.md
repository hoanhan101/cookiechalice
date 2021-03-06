# cookiechalice

cookiechalice is a [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for jumpstarting [AWS Chalice](https://github.com/aws/chalice) applications quickly. It supports:
- Makefile for generating build/test/deploy targets.
- [bison](https://github.com/edaniszewski/bison) for configuration.
- [containerlog](https://github.com/vapor-ware/containerlog) for structured logging.
- [requests](https://github.com/psf/requests) for HTTP support.
- [black](https://github.com/psf/black), [isort](https://github.com/PyCQA/isort), [mypy](https://github.com/python/mypy) for linting.
- [pytest](https://github.com/pytest-dev/pytest) for testing.

To create a new project:
```
cookiecutter https://github.com/hoanhan101/cookiechalice.git
```

Setup the project and install dependencies:
```
make setup
```

Run the project locally:
```
make local
```
