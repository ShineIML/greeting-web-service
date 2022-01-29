FROM python:3.9.10

WORKDIR /web-service

COPY requirements.txt .

RUN pip install -r requirements.txt && rm requirements.txt

COPY . .

ENV FLASK_APP="start.py" FLASK_DEBUG=1 DATABASE_URL=postgres://jbduzvmgcsebtb:27f5e32b0cebfa3ca9171208a59eda40e00cd70a99d810eccf30c61a66b526ba@ec2-54-73-152-36.eu-west-1.compute.amazonaws.com:5432/dasvmqpo1ebrjj

CMD [ "flask", "run", "--host=0.0.0.0"]