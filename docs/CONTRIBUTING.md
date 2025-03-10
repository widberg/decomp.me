# Contributing

## Directory structure
```
frontend/
  public/        ; Static files
  src/           ; React/Typescript sourcecode

backend/
  compilers/     ; Compiler binaries and configuration
  coreapp/       ; API Django app
    migrations/  ; Database migrations (generated by Django)
  decompme/      ; Main Django app
  libraries/     ; Library headers

.env             ; Default configuration
.env.local       ; Local configuration overrides (not checked-in)
```

## Setup

See [DOCKER.md](DOCKER.md) for instructions on how to run the project in a Docker container. Otherwise, continue reading this guide.

Dependencies:
- Python >=3.10
- Node.js >=14
- [Yarn](https://yarnpkg.com/getting-started/install)
- [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)

---
Create a file to hold environment variables:
```shell
touch .env.local
```

### Backend
```shell
cd backend
```

* Install Python dependencies with [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
```shell
poetry install
```

- Install compilers
```shell
poetry run python compilers/download.py
```

- Install libraries
```shell
poetry run python libraries/download.py
```

- Set up the database
```shell
poetry run python manage.py migrate
```

- Start the API server
```shell
poetry run python manage.py runserver
```

---

### Frontend
```shell
cd frontend
```

- Install dependencies
```shell
yarn
```

- Start the development webserver
```shell
yarn dev
```

- Access the site via [http://localhost:8080](http://localhost:8080)


### Optional steps
- [Configure vscode for development](VSCODE.md)
- [Configure wine for Windows compiler on Linux](WINE.md)
- [Set up GitHub authentication](GITHUB.md)
- [Install nsjail to run the compiler sandbox](SANDBOX.md)
- [Configure an nginx reverse proxy](NGINX.md)
- Download [wibo](https://github.com/decompals/WiBo/releases/latest) and add it to your system path (for running Windows compilers from Linux)


## Notes

### Updating the database

If you modify any database models (`models.py`), you'll need to run the following to update the database:
```shell
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```

### Running tests

To ensure everything is working properly, you can run the unit tests in the backend folder.

```shell
poetry run python manage.py test
```

### Frontend styling

We use Tailwind CSS with Radix UI colors. Each color is on a scale from 1 to 12 (inclusive), each with [a well-defined meaning](https://www.radix-ui.com/docs/colors/palette-composition/understanding-the-scale).

## Linting

- Check frontend
```shell
cd frontend
yarn lint
```

- Autofix frontend
```shell
cd frontend
yarn lint --fix
```

- Check backend
```shell
cd backend
poetry run mypy
poetry run black .
```
