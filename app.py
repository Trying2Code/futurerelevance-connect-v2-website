from flask import Flask, redirect, url_for, render_template, jsonify

app = Flask(__name__)

JOBS = [
 {
  'id': 1,
  'title': 'Python Programmer',
  'location': 'Cape Town, South Africa',
 'salary': 'R80,000.00pm'
 },
{
  'id': 2,
  'title': 'Data Analyst',
  'location': 'Cape Town, South Africa',
 'salary': 'market related'
 },
{
  'id': 3,
  'title': 'Front-end Engineer',
  'location': 'Cape Town, South Africa',
 'salary': 'R45,000.00pm'
 },
{
    'id': 3,
    'title': 'Java Developer',
    'location': 'Remote, South Africa',
   'salary': 'R45,000.00pm'
},
  {
      'id': 3,
      'title': 'Full-Stack Developer',
      'location': 'Remote, South Africa',
     'salary': 'Market Related'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='FuturRelevance Connect')

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/frequently")
def frequently_page():
    return render_template('frequently.html')

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)


  

  