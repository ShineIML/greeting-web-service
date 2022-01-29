## [Greeting-web-service](https://greetings-web-service.herokuapp.com/)

Needed to write a web service. On the main page, there is a form with a name input field and a "Greet" button. When you click on the button, if the name is encountered for the first time, enter "Hello, <Name>". If you have already met such a Name, Enter "I saw you, <Name>".

## About development

Since this was my first task to develop a web application, the first solution was to develop a program by storing user data in a set-collection. Later, a local postgres database was added to store data in a table deployed on the docker. And as a result, when deployed on a cloud service, a database deployed on heroku.

## Used
`python` `flask` `flask-sqlalchemy` `postgresql` `docker`
