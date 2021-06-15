# my_portfolio
A repo that allows the creation of a custom web application

## Content:
1. Info
2. Structure
3. Notes
4. How to Run

## Info

This is a python flask application that deploys a portfolio server, which can be used to display a 
personal web, that contains some information and details about a person. It works by using flask to deploy
some template html pages, which are link together and contain different aspects for an individual. The
Project has the following structure:

[comment]: <> (# ToDo: Add project structure here!!)

This project can be hosted using Heroku or pythonanywhere, and is compatible with any browser.

The contact page, uses requests and POST methods to upload sent information from the website to a csv file,
or a database. You can check the method through the server.py file. 

## How to run:

In a terminal use the following commands:

```
set FLASK_APP=server.py
flask run
```

This wil launch a website that will be hosted on your local port. In order to enable debug mode while running
please use the following:
```
set FLASK_APP=server.py
set FLAS_ENV=development
flask run
```
