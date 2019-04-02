from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy.orm import backref

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@123@localhost/test'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)


manager = Manager(app)
manager.add_command('db', MigrateCommand)
'''
asc=db.Table('subs',
    db.Column('keytostudent',db.Integer,db.ForeignKey('student.id')),
    db.Column('keytoclass',db.Integer,db.ForeignKey('class.id'))
)
'''
class Student(db.Model):
    __tablename_ = 'student'
    id = db.Column(db.String(250), primary_key=True)
    name = db.Column(db.String(80))
    class_id = db.Column(db.String(250),db.ForeignKey('class.id'))
    created_on = db.Column((db.String(250)))
    updated_on = db.Column(db.String(250))
    classes = db.relationship('Class', backref=db.backref('student', lazy='dynamic'))

class Class(db.Model):
    __tablename_ = 'class'
    id = db.Column(db.String(250), primary_key=True)
    name = db.Column(db.String(80))
    class_leader = db.Column(db.String(250),db.ForeignKey('student.id'))
    created_on = db.Column((db.String(250)))
    updated_on = db.Column(db.String(250)) #db.DateTime, index=True, default=datetime.utcnow
    students = db.relationship('Student', backref=db.backref('class', lazy='dynamic'))


if __name__ == '__main__':
    manager.run()
    app.run(debug=True)

    # classes = db.relationship('Class',backref=db.backref('student', lazy='dynamic'))
    #, secondary = asc