# thinker_cooker
This is a project for learning proposes.

The objective is get a list with the 5 better recipes that you can make with the ingredients you have in home.
For this 

## Create a virtual environment
`python3 -m venv .venv`

Activate the venv:

`source .venv/bin/activate`

Install requirements 

`pip install -r requirments.txt`

## Project Structure
The scrapper.py file have the necessary process to scrapping the first webpage and load the recipes in one xlsx file. I use [Recetas Gratis](www.recetasgratis.net) page and this web doesn't have one page where we have a complete list with all recipes of the site, so the script require we send the main category url to start looking and saving recipes.

QAgkt3BvuCrsQEMA
admin

## AirFlow
To run Airflow, follow the steps:

Airflow needs a home. `~/airflow` is the default, but you can put it

Somewhere else if you prefer (optional)
 

`export AIRFLOW_HOME=~/airflow`

If you don't want the default examples, set the follow environment variable:

`export AIRFLOW__CORE__LOAD_EXAMPLES=false` WORKS??

`AIRFLOW_VERSION=2.2.3`

`CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-2.2.3/constraints-3.X.txt"` Change the X for your python version 

`pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"`

for run 
`airflow standalone`

# Postgres

docker-compose up --build 

psql -h localhost -p 5432 -d test_db -U root 

when ask the pass is:
root



