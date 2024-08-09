from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
  {
    'id':1,
    'title':"Data analyst",
    'location':'Bangluru, India',
    'salary': '1000000',
  },
  {
    'id':2,
    'title':"front end",
    'location':'delhi, India',
    'salary': '1000000',
  },
  {
    'id':3,
    'title':"back end",
    'location':'Bombay, India',
    'salary': '1000000',
  },
  {
    'id':4,
    'title':"ML engineer",
    'location':'Bangluru, India',
    'salary': '1000000',
  },
]

# lets us assume that this  jobs list is comming from a dsatabase 

# we need a method to send this method into home.html

@app.route("/")
def hello_world():
  return render_template("home.html", jobs = jobs)



# sometime data is also provided by an API in json format
# here is how to use that to generate a dynamic html page
@app.route("/jobs")
def list_jobs():
  return jsonify(jobs)

# now this route (that is https://00ecd577-67de-4a84-a31e-e58d2320af82-00-19wa2ucjr4g58.sisko.replit.dev/jobs ) is actally gives a json ... which we will use in html 

if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug = True)