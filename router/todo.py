from flask import Blueprint, render_template, redirect, url_for, request
from sqlalchemy.sql import func
from database.db import db
from models.todo import Todo

todo_bp = Blueprint('todo_bp', __name__)


@todo_bp.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@todo_bp.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    body = request.form.get("body")
    new_todo = Todo(title=title, complete=False, body=body)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("todo_bp.home"))


@todo_bp.route("/update_form/<int:todo_id>")
def update_form(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()

    return render_template("update.html", data=todo)


@todo_bp.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    update_dt = func.now()
    todo.updated_at = update_dt
    db.session.commit()
    return redirect(url_for("todo_bp.home"))


@todo_bp.route("/update_todo/<int:todo_id>", methods=["POST"])
def update_todo(todo_id):
    title = request.form.get("title")
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.title = title
    update_dt = func.now()
    todo.updated_at = update_dt
    db.session.commit()
    return redirect(url_for("todo_bp.home"))


@todo_bp.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todo_bp.home"))
