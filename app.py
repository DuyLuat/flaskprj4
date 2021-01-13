#app.py
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for, render_template, Flask
import pymysql

db = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           database='test',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
app = Flask(__name__)
       
app.secret_key = "caircocoders-ednalan"
       

 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route("/postskill",methods=["POST","GET"])
def postskill():
    cur = db.cursor()
    msg=''
    if request.method == 'POST':
        skills = request.form.getlist('skill[]')
        for value in skills:  
            cur.execute("INSERT INTO skills (skillname) VALUES (%s)",[value])
            db.commit()       
        cur.close()
        msg = 'New record created successfully'    
    return jsonify(msg)
 
if __name__ == "__main__":
    app.run(debug=True)