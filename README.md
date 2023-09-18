# Seazone coding challenge by Matheus Araujo

## Solution
This solution consists of 3 APIs responsible for listing and creating the objects and 3 APIs responsible for the other operations.
An example of request follows:
- `GET /imoveis/` - List all imoveis
- `POST /imoveis/` - Create a new imovel
- `GET /imoveis?id=1` - Get a specific imovel
- `PATCH /imoveis/1/` - Update a specific imovel
- `DELETE /imoveis/1/` - Delete a specific imovel

Notice that `/imoveis/` is responsible for listing and creating the objects, while `/imoveis/{id}` is responsible for the other operations.

These are the APIs:
- `/imoveis/`
- `/imoveis/{id}`
- `/anuncios/`
- `/anuncios/{id}`
- `/reservas/`
- `/reservas/{id}`

The database was set up using docker-compose, so it's easy to run the project locally.

## How to run
- Clone this repository
- Use `pip install -r requirements.txt` to install dependencies
- Run `inv prepare-environment` to get the environment ready for the next 2 steps
- Once the environment is ready, run `inv prepare-db-for-tests` to apply all migrations and load test data
- Run `inv runserver` to start the server and test the APIs yourself
- Finally, run `inv run-tests` to run the unit tests