# Refactoring Project

Please do not fork this repository, but use this repository as a template for your refactoring project. Make Pull Requests to your own repository even if you work alone and mark the checkboxes with an `x`, if you are done with a topic in the pull request message.

## Project for today

The task for today you can find in the [project-for-today.md](./project-for-today.md) file.

## Setup

The necessary libraries are listed in the [requirements.txt](./requirements.txt) file. You can install them with the following command:

```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## My Experience

- What are the steps you took to complete the project?
1.  I read the notebook to understand the preprocessing steps
2. I copied the notebook; deleted descriptions, non-preprocessing code and the modelling part
3. I wrote preprocessing steps as functions in dataprep_for_king_county.py
4. I wrote a python file that uses preprocessing functions and prints out 4 sample houses with 5 features
```bash
python3 preprocessing/pipeline_4sample_5features.py
```
5. I added a .env file for environment variables

6. I setup a fastapi service folder with files main.py, models.py, database.py and a new requirements.txt for the fastapi app

```bash
pip install -r service/requirements.txt
```
7. I ran a postgres docker container: I opened Docker Desktop, got id of postgres container
```bash
docker ps -a
```
```bash
docker start CONTAINER_ID
```
8. I opened postgres, added a houses database, connected to database and created a table
```bash
psql -h localhost -p 5432 -U postgres
```

```SQL
CREATE DATABASE houses;
```
```SQL
\c houses;
```
```SQL
CREATE TABLE houses (
    table_id SERIAL PRIMARY KEY,
    id BIGINT,
    bedrooms INT,
    sqft_living INT,
    center_distance FLOAT,
    price FLOAT
);
```

9. in terminal I ran FastAPI and added data via POST functionality
```bash
cd service/
uvicorn main:app --reload --port 8100
```
```bash
curl -X POST http://localhost:8100/houses -H "Content-Type: application/json" -d '{"id": 4027701265, "bedrooms": 3, "sqft_living": 2920, "center_distance": 15.55402307333386, "price": 480000.0}'
```

10. after 3 more added houses, I displayed the database content

```bash
curl http://localhost:8100/houses
```
-> shows all the 4 added houses with 5 features

11. I created a Dockerfile for the FastAPI app


### My personal thoughts
- What are the challenges you faced?
1. it was challenging to add the sample data to the FastAPI, because of sensitivity towards quote types ("" and ''), double id variables (house id and table id) and some house ids needed bigint datatype for the postgres database
2. fastapi was not displayed on localhost on my system (wsl2)
- What are the things you would do differently if you had more time?
1. play with different fastAPI examples
2. alter database via update and delete functionality of the fastapi app
