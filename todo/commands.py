from datetime import datetime

import click

from todo import models
from todo.extensions import db


@click.command()
@click.argument("task")
def create_todo(task):
    today = datetime.today().date()
    todo = models.Todo(description=task, due_date=today, completed=False)
    print(todo.to_dict())
    db.session.add(todo)
    db.session.commit()
