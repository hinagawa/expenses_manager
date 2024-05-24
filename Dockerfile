FROM python:3.12

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=myproject.settings
ENV PYTHONUNBUFFERED 1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
