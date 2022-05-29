# Backend

## Технологии

* Python (FastAPI)
* PostgreSQL

## Вы можете развернуть всё в приложение в докере (включая базы данных)

__Backend__
```bash
docker-compose up --build -d
```

__Postgres__
```bash
cd docker
docker-compose up --build -d
```

## Либо развернуть в виртуальном окружении

## Запуск Linux / Mac

```console
foo@bar:~$ cd simple
foo@bar:~$ virtualenv env
foo@bar:~$ source env/bin/activate
foo@bar:~$ pip install -r requirements.txt
foo@bar:~$ git clone https://github.com/wildview2/neuro
```

## Запуск Windows

```console
foo@bar:~$ cd simple
foo@bar:~$ virtualenv env
foo@bar:~$ env/Scripts/activate.ps1
foo@bar:~$ pip install -r requirements.txt
foo@bar:~$ git clone https://github.com/wildview2/neuro
```
# Добавляем веса в /neuro с нашего  гугл диска (500 эпох):
https://drive.google.com/file/d/1-L6-CsiTX17NIIQbuRWtqHJEz6evjGNP/view?usp=sharing
#Переимновываем best.pt -> wildview.pt
