settings frontend

### 1. First.

Налить кофе, помыть руки

### 2. Development
`chmod +x start_dev.sh`

```
docker-compose -f docker-compose-dev.yml up --build

```

### 3. Production
`cd backend`

`chmod +x start_prod.sh`

`cd ..`


```
docker-compose up --build
```

```docker exec -it <id container> bash
    docker exec -it <id container> <command>

```
Database dump/load
```python manage.py dumpdata --natural-foreign --natural-primary --exclude=contenttypes --exclude=auth.Permission --indent 4 > default_data.json

python manage.py loaddata default_data.json
```


