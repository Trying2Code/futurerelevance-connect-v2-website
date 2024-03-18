from flask import Flask,render_template

app = Flask(__name__)

JOBS = [
 {
  'id': 1,
  'title': 'Python Programmer',
  'location': 'Cape Town, South Africa',
 'salary': 'market related'
 },
{
  'id': 2,
  'title': 'Data Analyst',
  'location': 'Cape Town, South Africa',
 'salary': 'market related'
 },
{
  'id': 3,
  'title': 'Front-end developer',
  'location': 'Cape Town, South Africa',
 'salary': 'market related'
 }

]
@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)