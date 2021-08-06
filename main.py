from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///beaches.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Beach(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(250), nullable=False)
    map_url=db.Column(db.String(500), unique=True, nullable=False)
    img_url=db.Column(db.String(500), unique=True, nullable=False)
    country=db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    has_admission=db.Column(db.Boolean, nullable=False)

db.create_all()

@app.route("/")
def home():
    all_beaches = Beach.query.all()
    #print(all_beaches[0].name)
    return render_template("index.html", beaches=all_beaches)



if __name__ == '__main__':
    app.run(debug=True)








