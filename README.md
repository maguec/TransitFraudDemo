# Let's Catch Some Transit Fraudsters

This is a demo on how to catch some people trying to commit transit fraud

## Setup Gcloud 

```bash
gcloud auth application-default login
make instancecreate
make loadschema
```


## Get Python setup and load the Data

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./load_data.py
```

## Start Queryring

[Queries](./SampleQueries.md)

