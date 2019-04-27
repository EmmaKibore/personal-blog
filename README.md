# PERSONAL BLOG
by Emma Kibore

## User Requirements
As a user I would like to view the blog posts submitted As a user I would like to comment on blog posts As a user I would like to view the most recent posts As a user I would like to alerted when a new post is made by joining a subscription.

## Writer Requirements
As a writer I would like to sign in to the blog. As a writer I would also like to create blog from the application. As a writer I would like to delete comments that I find insulting or degrading. As a writer I would like to update or delete blogs i have created.

## Specifications
SPECS.md

## Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.

Python 3.6

Cloning the repository
git clone https://github.com/EmmaKibore/Personal-Blog.git

## Database migrations
first initialize the database if the migrations folder does not exist
python manage.py db init

create a migration
python manage.py db migrate -m "initial migration"

upgrade
python manage.py db upgrade

insert initial data
python manage.py insert_initial_data

Installing dependencies
pip3 install -r requirements

Prepare environmet variables
In start.sh file, in the root folder

export MAIL_USERNAME=YOUR EMAIL export MAIL_PASSWORD=EMAIL PASSWORD export ADMIN_MAIL_USERNAME=ADMIN ACCOUNT EMAIL

Creating a virtual environment
python2.7 -m virtualenv virtual-blog source virtual-blog/bin/activate

Running Tests
python3.6 manage.py test

Live Demo
The web app can be accessed from the following link click here

## Technology used
Python3.6

Flask

Heroku

Bootstrap

Contributing
Git clone https://github.com/MutumaMutuma/Personal-Blog.git

## License
MIT License

© Emma Kibore