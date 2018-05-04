# Logistiko

Sample project for emulating the Business Intelligence dashboards of logistics applications.

## Requirements

* Python 3.6+
* PostgreSQL 10.3+

## Dependencies

This project uses [pipenv](https://github.com/pypa/pipenv) to install Python dependencies.

## Getting Started

Create an alias for `pipenv run python app.py` in your `~/.bash_profile`:

```
alias app="pipenv run python app.py"
```

Install project dependencies:

```
$ pipenv install
```

Create a user and database in PostgreSQL by running `sudo -u postgres psql`:

```
# create role and database
CREATE USER logistiko_user WITH PASSWORD 'YOUR-STRONG-PASSWORD';
CREATE DATABASE logistiko_db;

# update database definitions
ALTER USER logistiko_user CREATEDB;
ALTER ROLE logistiko_user SET client_encoding TO "utf8";
ALTER ROLE logistiko_user SET default_transaction_isolation TO "read committed";
ALTER ROLE logistiko_user SET timezone TO "UTC";
GRANT ALL PRIVILEGES ON DATABASE logistiko_db TO logistiko_user;

# exit
\q
```

Set your environment variables in the `.proj-env` file:

```
$ cp .proj-env.example .proj-env
$ vi .proj-env
```

## Initialize the database

```
$ app init db
```

## Load data from existing Excel and CSV files

```
$ app load analysis <path/to/file.ext>
$ app load sales_order --status <path/to/file.ext>
$ app load sales_order --item <path/to/file.ext>
$ app load sales_order --history <path/to/file.ext>
```

## Running the server and viewing the dashboard

```
$ app run
```

## License

MIT. See [LICENSE.md](LICENSE.md) for more details.
