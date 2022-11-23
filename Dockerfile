FROM python

MAINTAINER Mohammed Bilal <bilal00717@gmail.com>

WORKDIR /app

COPY /requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver","0.0.0.0:5000"]
