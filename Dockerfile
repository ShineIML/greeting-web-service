FROM python:3.9.10

WORKDIR /web-service

COPY requirements.txt .

RUN pip install -r requirements.txt && rm requirements.txt

COPY . .

ENV FLASK_APP="start.py" FLASK_DEBUG=1 DATABASE_URL='postgresql://xdfhkkmhunxxim:5b2f2c590b5963a8bd3422bce0283a7730a9b0dea7ee2a7580e15ee291f7e8d6@ec2-34-242-89-204.eu-west-1.compute.amazonaws.com:5432/d1r7qn9gh3f6ug'

CMD [ "flask", "run", "--host=0.0.0.0"]