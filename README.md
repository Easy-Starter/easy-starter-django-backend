<div align="center">

# Easy Starter Django Backend

**A production-capable Django backend with admin, API foundations, PostgreSQL, Docker, tests, and secure environment configuration.**

[![Use this template](https://img.shields.io/badge/Use%20this%20template-2ea44f?logo=github&logoColor=white)](https://github.com/easy-starter/easy-starter-django-backend/generate) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Status: foundation](https://img.shields.io/badge/status-foundation-orange) ![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) ![uv](https://img.shields.io/badge/uv-DE5FE9?logo=uv&logoColor=black)

[فارسی](README.fa.md) · [Documentation](https://github.com/easy-starter/easy-starter-docs) · [Report an issue](https://github.com/easy-starter/easy-starter-django-backend/issues/new/choose)

</div>

> “What do we build for, if not to lessen each other’s hardship?”

> [!IMPORTANT]
> This repository is currently in the **foundation stage**. Do not treat it as production-ready until the first stable release.

## What it solves

Provides a consistent backend foundation so projects start with secure settings, clear app boundaries, repeatable local development, and production checks.

## Use this template for

- REST APIs and business backends
- Django Admin-based operations
- Backends for Next.js, mobile apps, bots, and extensions
- Data-heavy and workflow-driven products

**Not intended for:** A microservice fleet or a prebuilt domain model for every business.

## Baseline

- Environment-specific settings and validation
- Custom user model and admin foundations
- PostgreSQL, migrations, health checks, and structured logging
- Docker-based local and production workflows
- Tests, linting, type checks, CI, and deployment checklist

Detailed architecture, conventions, deployment profiles, and extension guides belong in [`docs/`](docs/). Feature work starts from [`specs/`](specs/), and agent rules live in [`AGENTS.md`](AGENTS.md).

## Quick start

1. Click **Use this template** or run:

   ```bash
   gh repo create my-project --template easy-starter/easy-starter-django-backend --private --clone
   cd my-project
   ```

2. Set the project name, package metadata, and environment values.
3. Start the project:

   ```bash
   cp .env.example .env
   make setup
   make dev
   make check
   ```

4. Write the first feature specification under `specs/`.
5. Implement the feature and keep `make check` green.

## Working agreement

- Read `AGENTS.md` and the relevant specification before changing code.
- Reuse existing patterns before adding abstractions or dependencies.
- Never commit credentials or production data.
- Run the repository quality checks before opening a pull request.
- Record architecture-changing decisions in `docs/decisions/`.

## Documentation

Start with `docs/getting-started.md`. Broader AI-first development guidance is maintained in [Easy Starter Docs](https://github.com/easy-starter/easy-starter-docs).

## Contributing and support

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for contribution rules and [`SUPPORT.md`](SUPPORT.md) for help. Security issues must follow [`SECURITY.md`](SECURITY.md).

## License

Released under the [MIT License](LICENSE).

<!--


## 📖 Installation

**Easy Starter Django** can be installed via Pip or Docker. To start, clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/Easy-Starter/easy-starter-django.git
$ cd easy-starter-django
```

### uv

You can use [uv](https://docs.astral.sh/uv/) to create a dedicated virtual environment.

```
$ uv sync
```

Then run `migrate` to configure the initial database. The command `createsuperuser` will create a new superuser account for accessing the admin. Execute the `runserver` command to start up the local server.

```
$ uv run manage.py migrate
$ uv run manage.py createsuperuser
$ uv run manage.py runserver
# Load the site at http://127.0.0.1:8000 or http://127.0.0.1:8000/admin for the admin
```

### Docker

To use Docker with PostgreSQL as the database update the `DATABASES` section of `easy_starter_django/settings.py` to reflect the following:

```python
# easy_starter_django/settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",  # set in docker-compose.yml
        "PORT": 5432,  # default postgres port
    }
}
```

The `INTERNAL_IPS` configuration in `easy_starter_django/settings.py` must be also be updated:

```python
# config/settings.py
# django-debug-toolbar
import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
```

And then proceed to build the Docker image, run the container, and execute the standard commands within Docker.

```
$ docker compose up -d --build
$ docker compose exec web python manage.py migrate
$ docker compose exec web python manage.py createsuperuser
# Load the site at http://127.0.0.1:8000 or http://127.0.0.1:8000/admin for the admin
```

## Create new repo from the template

- change all the easy_starter_django in the project
- Ctrl + Shift + F -> search "easy_starter_django" -> replace all with Ctrl + Shift + H
- remove .env track from git

```bash
git rm --cached -- .env.*
```

```bash
pip install django-environ dj_database_url psycopg
```

- Create new SECRET_KEY and put it in your .env files

‍‍‍```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

````

- Add .env.* to .gitignore

```bash
export DJANGO_ENV=dev  # for running on local server
````


```bash
sudo -u postgres psql  # Run psql


CREATE USER myuser WITH PASSWORD 'mypassword';  # Create new user

CREATE DATABASE mydb OWNER myuser;  # Create new DB

\q  # Quit psql
```

- DB URL pattern to use as a DATABSE_URL env variable value:

postgresql://{env('DB_USER')}:{env('DB_PASSWORD')}@localhost:5432/{env('DB_NAME')}

- Apply migrations

```bash
ptyhon manage.py migrate
``` -->
