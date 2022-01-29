FROM python:3.9.10

WORKDIR /web-service

COPY requirements.txt .

RUN pip install -r requirements.txt && rm requirements.txt

COPY . .

ENV FLASK_APP="start.py" FLASK_DEBUG=1 DATABASE_URL=postgres://$(whoami)

CMD [ "flask", "run", "--host=0.0.0.0"]