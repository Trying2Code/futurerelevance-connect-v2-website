from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']


engine  = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),  {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()
      
def add_application_to_db(job_id, data):
  with engine.connect() as conn: 
    query = text("INSERT INTO applications (job_id, first_name, last_name, email, street_address, unit_suburb, city, country, area_code, education, work_experience, resume_url) values (:job_id, :first_name, :last_name, :email, :street_address, :unit_suburb, :city,  :country,  :area_code, :education, :work_experience, :resume_url)")

    conn.execute(query, {"job_id": job_id, "first_name": data['first_name'], "last_name": data['last_name'], "email": data['email'], "street_address" : data['street_address'], "unit_suburb" : data['unit_suburb'], "city" : data['city'], "country" : data['country'], "area_code" : data['area_code'], "education" : data['education'], "work_experience" : data['work_experience'], "resume_url" : data['resume_url']})
                 
                 

      
      