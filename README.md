#Rpack-registry
Manage account.

##Document
###install django package

    pip install -r django-pkg.txt

###bower install

    python manage.py bower install
###start the django
First you have to install the django and django-rest-framework

Create database

    python manage.py syncdb

Start server

    python manage.py runserver

### Gulp for build

#### prerequisite

Install nodejs, npm

```
sudo npm install -g gulp
```

and 

```
npm install
```

After install all necessaries enter

```
gulp # build less to css
```

**NOTE:** css stylesheets should not code in `static/stylesheets/`, code in `static/less` and gulp will compile to css for you.


##License
Apache 2.0 by Rfirm
