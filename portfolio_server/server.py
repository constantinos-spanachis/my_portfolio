from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:file>")
def index(file: str = None):
    return render_template(file)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        write_to_csv(data)
        return redirect('/thank_you.html')
    else:
        return "Failed to submit form"


def write_to_csv(data):
    import csv
    with open("database.csv", newline='', mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        writter = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writter.writerow([email, subject, message])
        database2.close()
   

def write_to_file(data):
    with open('database.txt', mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")
        database.close()
