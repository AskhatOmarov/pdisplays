install mysql-server and client
sudo apt-get install mysql-server mysql-client

install mysql connector for python
sudo apt-get install python-mysqldb
sudo apt-get install libmysqlclient-dev

mkdir pdisplays
virtualenv --no-site-packages venv
. ./venv/bin/activate

cd pdisplays
git clone git@github.com:AskhatOmarov/pdisplays.git
pip install -r requirements.txt

create database 'pdisplays' in mysql

python manage.py syncdb
python manage.py migrate
python manage.py runserver