from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

@app.route("/")
def hello_FutureRelevavce():
  jobs = load_jobs_from_db()
  return render_template('home.html',
                         jobs=jobs,
                         company_name='FuturRelevance Connect')

@app.route("/login")
def login_page():
    return render_template('login.html')

@app.route("/signup")
def signup_page():
    return render_template('signup.html')

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/frequently")
def frequently_page():
    return render_template('frequently.html')

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template('jobpage.html', job=job)    
    

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)


  

  