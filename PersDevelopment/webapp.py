#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime
import statistics

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'
app.config.update(
    DEBUG=True,
    #EMAIL SETTING
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME= 'personal.development.form@gmail.com',
    MAIL_PASSWORD= 'haslo1231'
)
mail = Mail(app)
db = SQLAlchemy(app)


class Formdata(db.Model):
    __tablename__ = 'formdata'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    sex = db.Column(db.String)
    education = db.Column(db.String)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)
    q6 = db.Column(db.Integer)
    q7 = db.Column(db.Integer)
    q8 = db.Column(db.Integer)
    q9 = db.Column(db.Integer)
    q10 = db.Column(db.Integer)
    q11 = db.Column(db.Integer)
    q12 = db.Column(db.Integer)
    q13 = db.Column(db.Integer)
    q14 = db.Column(db.Integer)
    q15 = db.Column(db.Integer)
    q16 = db.Column(db.Integer)
    q17 = db.Column(db.Integer)

    def __init__(self, name, email, sex, education, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14,
                 q15,q16, q17):
        self.name = name
        self.email = email
        self.sex = sex
        self.education = education
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.q10 = q10
        self.q11 = q11
        self.q12 = q12
        self.q13 = q13
        self.q14 = q14
        self.q15 = q15
        self.q16 = q16
        self.q17 = q17


db.create_all()


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/form")
def form():
    return render_template('form.html')


@app.route("/statistics")
def show_result():
    fd_list = db.session.query(Formdata).all()
    sex_male = db.session.query(Formdata).filter_by(sex='male').count()
    sex_female = db.session.query(Formdata).filter_by(sex='female').count()
    sex_other = db.session.query(Formdata).filter_by(sex='others').count()

    education_primary = db.session.query(Formdata).filter_by(education='primary').count()
    education_secondary = db.session.query(Formdata).filter_by(education='secondary').count()
    education_higher = db.session.query(Formdata).filter_by(education='higher').count()

    # Some simple statistics for sample questions
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    q5 = []
    q6 = []
    q7 = []
    q8 = []
    q9 = []
    q10 = []
    q11 = []
    q12 = []
    q13 = []
    q14 = []
    q15 = []
    q16 = []
    q17 = []

    for el in fd_list:
        q1.append(int(el.q1))
        q2.append(int(el.q2))
        q3.append(int(el.q3))
        q4.append(int(el.q4))
        q5.append(int(el.q5))
        q6.append(int(el.q6))
        q7.append(int(el.q7))
        q8.append(int(el.q8))
        q9.append(int(el.q9))
        q10.append(int(el.q10))
        q11.append(int(el.q11))
        q12.append(int(el.q12))
        q13.append(int(el.q13))
        q14.append(int(el.q14))
        q15.append(int(el.q15))
        q16.append(int(el.q16))
        q17.append(int(el.q17))

    if len(q1) > 0:
        mean_q1 = statistics.mean(q1)
    else:
        mean_q1 = 0

    if len(q2) > 0:
        mean_q2 = statistics.mean(q2)
    else:
        mean_q2 = 0

    if len(q3) > 0:
        mean_q3 = statistics.mean(q3)
    else:
        mean_q3 = 0

    if len(q4) > 0:
        mean_q4 = statistics.mean(q4)
    else:
        mean_q4 = 0

    if len(q5) > 0:
        mean_q5 = statistics.mean(q5)
    else:
        mean_q5 = 0

    if len(q6) > 0:
        mean_q6 = statistics.mean(q6)
    else:
        mean_q6 = 0

    if len(q7) > 0:
        mean_q7 = statistics.mean(q7)
    else:
        mean_q7 = 0

    if len(q8) > 0:
        mean_q8 = statistics.mean(q8)
    else:
        mean_q8 = 0

    if len(q9) > 0:
        mean_q9 = statistics.mean(q9)
    else:
        mean_q9 = 0

    if len(q10) > 0:
        mean_q10 = statistics.mean(q10)
    else:
        mean_q10 = 0

    if len(q11) > 0:
        mean_q11 = statistics.mean(q11)
    else:
        mean_q11 = 0

    if len(q12) > 0:
        mean_q12 = statistics.mean(q12)
    else:
        mean_q12 = 0

    if len(q13) > 0:
        mean_q13 = statistics.mean(q13)
    else:
        mean_q13 = 0

    if len(q14) > 0:
        mean_q14 = statistics.mean(q14)
    else:
        mean_q14 = 0

    if len(q15) > 0:
        mean_q15 = statistics.mean(q15)
    else:
        mean_q15 = 0

    if len(q16) > 0:
        mean_q16 = statistics.mean(q16)
    else:
        mean_q16 = 0

    if len(q17) > 0:
        mean_q17 = statistics.mean(q17)
    else:
        mean_q17 = 0

    # Prepare data for google charts
    data = [['Male', sex_male],
            ['Female', sex_female],
            ['Others', sex_other],
            ['Primary',education_primary],
            ['Secondary',education_secondary],
            ['Higher',education_higher],
            ['Q1', mean_q1],
            ['Q2', mean_q2],
            ['Q3', mean_q3],
            ['Q4', mean_q4],
            ['Q5', mean_q5],
            ['Q6', mean_q6],
            ['Q7', mean_q7],
            ['Q8', mean_q8],
            ['Q9', mean_q9],
            ['Q10', mean_q10],
            ['Q11', mean_q11],
            ['Q12', mean_q12],
            ['Q13', mean_q13],
            ['Q14', mean_q14],
            ['Q15', mean_q15],
            ['Q16', mean_q16],
            ['Q17', mean_q17]]

    return render_template('statistics.html', data=data)


@app.route("/raw")
def show_raw():
    fd = db.session.query(Formdata).all()
    return render_template('raw.html', formdata=fd)


@app.route("/thankyou")
def thanks():
    return render_template('thanks.html')

@app.route("/thankyou2")
def thanks2():
    return render_template('thanks2.html')

@app.route("/emptyform")
def emptyform():
    return render_template('empty_form.html')


@app.route("/emptyfield")
def emptyfield():
    return render_template('empty_field.html')


@app.route("/usefully")
def usefully():
    return render_template('usefully.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/send_mail", methods=['POST'])
def send_mail():
    # Get data from FORM
    try:
        name = request.form['name']
        email = request.form['email']
        text = request.form['text']
        msg = Message(name + " " + email,
           sender="personal.development.form@gmail.com",
           recipients=["personal.development.form@gmail.com"])
        msg.body = "Wiadomość od: " + name + "\n" + \
                    "Email: " + email + "\n" \
                    "Treść: " + text + "\n"
        mail.send(msg)
        return redirect('/thankyou2')
    except Exception as e:
        return redirect('/emptyfield')



@app.route("/save", methods=['POST'])
def save():
    # Get data from FORM
    try:
        name = request.form['name']
        email = request.form['email']
        sex = request.form['gender']
        education = request.form['education']
        q1 = request.form['q1']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']
        q5 = request.form['q5']
        q6 = request.form['q6']
        q7 = request.form['q7']
        q8 = request.form['q8']
        q9 = request.form['q9']
        q10 = request.form['q10']
        q11 = request.form['q11']
        q12 = request.form['q12']
        q13 = request.form['q13']
        q14 = request.form['q14']
        q15 = request.form['q15']
        q16 = request.form['q16']
        q17 = request.form['q17']

        form_data = [name, email, sex, education, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15,
                     q16, q17]

        if form_is_empty(form_data):
            return redirect('/emptyform')

        if form_has_empty_field(form_data):
            return redirect('/emptyfield')
        else:
            # Save the data
            fd = Formdata(name, email, sex, education, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15,
                          q16, q17)
            db.session.add(fd)
            db.session.commit()

            return redirect('/thankyou')

    except Exception as e:
        return redirect('/emptyform')


def form_is_empty(form_data):
    is_empty = True

    for i in form_data:
        if i:
            is_empty = False

    return is_empty


def form_has_empty_field(form_data):
    has_empty = False

    for i in form_data:
        if not i:
            has_empty = True

    return has_empty


if __name__ == "__main__":
    app.debug = True
    app.run()
