# Rpack-registry

**Working in process**

Require:

- Django: 1.6.3
- Python: 2.x

Registry for Rpack




### Create a project using django

```
python /usr/local/lib/python2.7/site-packages/django/bin/django-admin.py startproject rpack_register
```

If you have the problem to find your `django-admin.py` go here: https://docs.djangoproject.com/en/1.6/faq/troubleshooting/#troubleshooting-django-admin-py

### Create users and group in django

https://docs.djangoproject.com/en/1.6/topics/auth/default/#topics-auth-creating-superusers

### Start server

```
python manage.py runserver
```

### Sync database

```
python manage.py syncdb
```

### Setting database

Using sqlite3

## License

MIT


## Reference

Tutorial:

- https://docs.djangoproject.com/en/1.6/intro/tutorial01/
