from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)


todo_list = []


class Task:
    def __init__(self, name, priority, due_date):
        self.name = name
        self.priority = priority
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")

    def __str__(self):
        return f"{self.name} | Prioritas: {self.priority} | Tenggat: {self.due_date.strftime('%Y-%m-%d')}"


@app.route("/")
def index():
    return render_template("index.html", tasks=todo_list)


@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        name = request.form["name"]
        priority = int(request.form["priority"])
        due_date = request.form["due_date"]
        try:
            task = Task(name, priority, due_date)
            todo_list.append(task)
            return redirect(url_for("index"))
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD."
    return render_template("add_task.html")


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    if 0 <= task_id < len(todo_list):
        del todo_list[task_id]
    return redirect(url_for("index"))


@app.route("/sort/priority")
def sort_by_priority():
    todo_list.sort(key=lambda task: task.priority)
    return redirect(url_for("index"))


@app.route("/sort/due_date")
def sort_by_due_date():
    todo_list.sort(key=lambda task: task.due_date)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
