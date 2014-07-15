
# Register account

```
curl -d "username=tmpAccount&password=tmpPassword&email=tmp@tmp.com" http://127.0.0.1:8000/users/
```

# Login account

```
curl -d "username=tmpAccount&password=tmpPassword" http://127.0.0.1:8000/signin/ -D cookie0001.txt
```

# Logout account

```
curl -i http://127.0.0.1:8000/logout/ -b cookie0001.txt
```

# Get session user's data

```
curl -i http://127.0.0.1:8000/users/me/ -b cookie0001.txt
```

#Get users data by username

```
curl -i http://127.0.0.1:8000/users/tmpAccount/
```
