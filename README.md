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
1.  run the notebook to understand the preprocessing steps
2. copied the notebook; deleted descriptions, non-preprocessing code and the modelling part
3. wrote preprocessing steps as functions in dataprep_for_king_county.py
4. wrote a python file that uses preprocessing functions and prints out 4 sample houses with 5 features
```bash
python3 preprocessing/pipeline_4sample_5features.py
```
5. added a .env file for environment variables

6. setup fastapi service folder with files main.py, models.py, database.py, requirements.txt

```bash
pip install -r service/requirements.txt
```
7. open and run docker container: open Docker Desktop, get id of postgres container
```bash
docker ps -a
```
```bash
docker start CONTAINER_ID
```
8. opened postgres, added database, connected to database, created the table
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

9. in terminal run FastAPI, added data with POST
```bash
cd service/
uvicorn main:app --reload --port 8100
```
```bash
curl -X POST http://localhost:8100/houses -H "Content-Type: application/json" -d '{"id": 4027701265, "bedrooms": 3, "sqft_living": 2920, "center_distance": 15.55402307333386, "price": 480000.0}'
```

10. after 3 more houses display database content

```bash
curl http://localhost:8100/houses
```
-> shows all the 4 added houses with 5 features

11. created Dockerfile for the FastAPI app


## personal thoughts
- What are the challenges you faced?
1. it was challenging to add the sample data to the FastAPI, because of double id variables (house id and table id) and some house ids needed bigint datatype for the postgres database
2. fastapi not displayed on localhost on my system (wsl2)
- What are the things you would do differently if you had more time?
1. play with simpler fastAPI examples
2. alter database with update and delete
