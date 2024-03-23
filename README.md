![python logo](https://www.python.org/static/community_logos/python-logo.png) 

<div align="center" style="padding-top: 5%; padding-bottom: 5%">
<i>Small dockerized backend project to showcase my coding skills using Python 3.11. 
Some packages used are FastAPI, SQLAlchemy, Pydantic and BeautifulSoup4.</i>
</div>


## Technical Description

### The focus of the project

The focus of the project is to serve a base project structure that can even serve as a template 
for a robust backend using generic approach. Implementation was written by applying the SOLID 
principles and paying particular attention to complexity management and maintainability.

### Choice of modules
As choice of web framework I have chosen FastAPI as it is a fast and popular web framework that 
makes it easy to implement production-ready code fast. FastAPI natively integrates well with 
Pydantic, that is why it is used for endpoint input parameter validation. For validation purposes 
the implementation also uses Pydantic before executing any of the CRUD operations. As for 
SQLAlchemy it is a widely used SQL toolkit and ORM that gives a lot of flexibility of SQL. By 
dockerizing the project it made it portable and easy to deploy to in-house or Cloud servers as well.

<p align="center" style="padding-top: 5%; padding-bottom: 5%"> <img 
src="https://github.com/hajnalkamarki/product-watcher-python-backend-with-fastapi/blob/master/docs/img/schema.png"
/></p>

## Usage

WIP 

## Features 

The features of the project used as a template:

<li>Project structure minimizes complexity</li>
<li>Provides multiple generic solutions and supports re-usability</li>
<li>Flexibility of databases (SQLite, Postgresql, MySQL, Oracle, MS-SQL, Firebird, Sybase and others 
that are supported by SQLAlchemy)</li>
<li>New components can be added easily</li>
<li>Provides solution examples for data validation that integrates well with FastAPI and SQLAlchemy.</li>
<li>Dockerization - WIP</li>
<li>Pre-commit integration - WIP</li>

## Use Case

The project was implemented with minimal functionality of a price watcher backend that helps monitoring 
product prices across different E-commerce websites.
