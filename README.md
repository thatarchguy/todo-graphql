# TODO

## About
This uses the Ariadne Graphql library. It's a _schema first_ library, which means the schema written in the SDL is the source of truth.

## Setting up

### Poetry
```
poetry install
poetry shell # activate the virtualenv
```

### Virtualenv
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


Create the database
```
python
>>> from main import db
>>> db.create_all()
>>>
```

Create a todo
```
flask create-todo "go for a run"

{'id': None, 'completed': False, 'description': 'go for a run', 'due_date': '08-02-2022'}
```

Run the app
```
export FLASK_APP=main.py
flask run
# OR
python main.py
```