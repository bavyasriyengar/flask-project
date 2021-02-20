from flask import Flask, render_template,request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:' 'user@123''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    amb_id = db.Column(db.Integer, primary_key=True)
    queue_id= db.Column(db.String(100))
    amount = db.Column(db.String(100))
    task_count = db.Column(db.String(100))
    state=db.Column(db.String(100))
    reason=db.Column(db.String(100))

    def __init__(self,amb_id,queue_id,amount,task_count,state,reason):
        self.amb_id=amb_id
        self.queue_id=queue_id
        self.amount=amount
        self.task_count=task_count
        self.state=state
        self.reason=reason




@app.route('/')
def Index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


