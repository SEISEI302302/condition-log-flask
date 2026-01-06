from flask import Flask, request, redirect, url_for, render_template_string

from db import init_db, add_log, fetch_logs, delete_log, get_log_by_id, update_log
from templates import HTML, EDIT_HTML

app = Flask(__name__)

@app.get("/")
def index():
    logs = fetch_logs()
    return render_template_string(HTML, logs=logs)

@app.post("/add")
def add():
    energy = int(request.form["energy"])
    mind = int(request.form["mind"])
    note = request.form.get("note", "").strip()

    if not (1 <= energy <= 10) or not (1 <= mind <= 10):
        return "energy/mind must be 1..10", 400

    add_log(energy, mind, note)
    return redirect(url_for("index"))

@app.post("/delete/<int:log_id>")
def delete(log_id):
    delete_log(log_id)
    return redirect(url_for("index"))

@app.get("/edit/<int:log_id>")
def edit(log_id):
    log = get_log_by_id(log_id)
    if not log:
        return "Not Found", 404
    return render_template_string(EDIT_HTML, log=log)

@app.post("/update/<int:log_id>")
def update(log_id):
    energy = int(request.form["energy"])
    mind = int(request.form["mind"])
    note = request.form.get("note", "").strip()

    if not (1 <= energy <= 10) or not (1 <= mind <= 10):
        return "energy/mind must be 1..10", 400

    update_log(log_id, energy, mind, note)
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True, use_reloader=False)
