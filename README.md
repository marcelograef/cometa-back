# Cometa Ejercicio

## Setup

1. Clone the repository
2. Create and activate the virtualenv

```
cd cometa-back
export VIRTUAL_ENV=.virtualenv/cometa-back
mkdir -p $VIRTUAL_ENV

virtualenv $VIRTUAL_ENV --python=python3.11
source .virtualenv/cometa-back/usr/local/bin/activate

```

1. Install dependencies: `pip install -r requirements.txt`
1. Run the server: `python manage.py runserver`

## API Endpoints

- `/api/order/`: Get order data

You can test it using CURL:
curl -H "Accept: application/json" http://127.0.0.1:8000/api/order/

## Running Tests

Run tests with the following command:

```sh
python manage.py test
```
