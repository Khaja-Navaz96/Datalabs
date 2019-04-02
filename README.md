# Datalabs


DATA MIGRATION: 

=> Install the following packages using command: " pip install 'package_name' "

Flask 1.0.2
Flask-Migrate 2.4.0
Flask-Script 2.0.6
Flask-SQLAlchemy 2.3.2
mysqlclient 1.4.2.post1
PyMySQL 0.9.3

=> Next,run the below commands

python migrate.py db init                //  creates a migration repository
python migrate.py db migrate            //  generates a migration script
python migrate.py db upgrade           //  executes the migration script,created using alembic
python migrate.py db downgrade        //  downgrade to the previous revision(undo execution) 
