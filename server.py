from os import name
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def page_name(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        Email = data["Email"]
        Subject = data["Subject"]
        Message = data["Message"]
        file=database.write(f'\n{Email}, {Subject}, {Message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        Email = data["Email"]
        Subject = data["Subject"]
        Message = data["Message"]
        csv_writer = csv.writer(database2, delimiter=';' , quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([Email,Subject,Message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "Ada yang salah. Coba cek lagi!"