from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime
import uuid
from time import gmtime, strftime

app = Flask(__name__, template_folder='/Users/10652578/Desktop/Pycharm_projects/Template/src')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@123@localhost/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Student(db.Model):
    __tablename_ = 'student'
    id = db.Column(db.String(250), primary_key=True)
    name = db.Column(db.String(80))
    class_id = db.Column(db.String(250))
    created_on = db.Column((db.String(250)))
    updated_on = db.Column((db.String(250)))

    def __init__(self, id, name, class_id, created_on, updated_on):
        self.id = id
        self.name = name
        self.class_id = class_id
        self.created_on = created_on
        self.updated_on = updated_on


class Class(db.Model):
    __tablename_ = 'class'
    id = db.Column(db.String(250), primary_key=True)
    name = db.Column(db.String(80))
    class_leader = db.Column(db.String(250))
    created_on = db.Column((db.String(250)))
    updated_on = db.Column(db.String(250))

    def __init__(self, id, name, class_leader, created_on, updated_on):
        self.id = id
        self.name = name
        self.class_leader = class_leader
        self.created_on = created_on
        self.updated_on = updated_on
        db.create_all()

@app.route('/insert', methods=['GET', 'POST'])
def Insert():
    data3 = Student.query.all()
    if request.method == 'POST':
        studentDetails = request.form
        name = studentDetails['name']
        unique = uuid.uuid1()
        unique1 = uuid.uuid1()
        date1 = datetime.datetime.now()
        date2 = None
        data1 = Student(unique, name, unique1, date1, date2)
        data2 = Class(unique1, name, unique, date1, date2)
        db.session.add(data1)
        db.session.commit()
        db.session.add(data2)
        db.session.commit()
        return redirect('/insert')
    return render_template('insert.html',Data1=data3)


@app.route('/')
def see():
    data2 = Student.query.all()
    return render_template('index.html', Data1=data2)


@app.route('/update', methods=['GET','POST'])
def up():
    data2 = Student.query.all()
    if request.method == 'POST':
        studentDetails = request.form
        name = studentDetails['name']
        ID=studentDetails['id']
        update_this = Student.query.filter_by(id=ID).first()
        update_this1 = Class.query.filter_by(class_leader=ID).first()
        update_this.name = name
        update_this1.name = name
        date1 = datetime.datetime.now()
        update_this.updated_on = date1
        update_this1.updated_on = date1
        db.session.commit()
    return render_template('update.html', Data1=data2)


# @app.route('/up/<int:id>', methods=['GET','POST'])
# def up(id):
#     if request.method == 'POST':
#         studentDetails = request.form
#         name = studentDetails['name']
#         update_this = Student.query.filter_by(name = id).first()
#         update_this.name = name
#         date1 = datetime.date.today()
#         update_this.update_on = date1
#         db.session.commit()
#     return render_template('index.html')


@app.route('/del', methods=['GET','POST'])
def dele():
    data2 = Student.query.all()
    if request.method == 'POST':
        studentDetails = request.form
        ID = studentDetails['id']
        del_this = Student.query.filter_by(id=ID).first()
        del_this1 = Class.query.filter_by(class_leader=ID).first()
        db.session.delete(del_this)
        db.session.commit()
        db.session.delete(del_this1)
        db.session.commit()
        return redirect('/del')
    return render_template('del.html', Data1=data2)



if __name__ == '__main__':
    app.run(debug=True)


