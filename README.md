## First Time Setup

Install virtualenv and activate

```virtualenv venv && source venv/bin/activate```

Install required packages

``` pip install -r req.txt ```

Install postgres and create database 'Blockchain'.
Look at config file for the env vars to be set

## Database development:
To create tables - you must run DDL in: ```create_db.txt ```

## Start server

To start the server
``` 
python main.py 
