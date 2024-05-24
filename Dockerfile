FROM python:3.12

WORKDIR /code

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV PYTHONUNBUFFERED 1

WORKDIR /code/expenses_manager

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
