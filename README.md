# pin-your-interests

## By Kelly Kiiru

## Description

This is a django application that allows users to View different photos that interest them.


## Table of Content

+ [Description](#description)
+ [Setup/Installation Requirements](setup&installationrequirements)
+ [BDD & TDD](#bdd&tdd)
+ [UserStory](#userstory)
+ [Technology & Tools](#technology&tools)
+ [Reference](#reference)
+ [Licence](#licence)
+ [Authors Info](#authors-info)




## Setup Installations Requirements
   * To run the application, in your terminal:

    1. Clone this [github repo] (https://github.com/KellyKiiru/pin-your-interests.git)
    2. Create a virtual environment
    3. Read the requirements file and Install all the requirements. Or run pip3 install -r requirements.txt to automatically install all the requirements
    4. Run server depending on your python interpreter
  
#### Prerequisites

You must have git, django, postgres and python3.8+ installed in your pc.
To install django and Postgres, you can use the following commands:

#django
$ pip install django

#postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev

### Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 


### Deployment environment
* Heroku

## BDD

|        User Requirements                 |           Input                           |           Output                         |
|------------------------------------------|-------------------------------------------|------------------------------------------|
| View all images                          |  Go to the home page                      |    All images will be displayed          |
| Search for an image                      | Input the category name in the search bar | All images in that category will display |
| View the image details                   | Click on the image                        | All the image details will be displayed  |
| Copy image                               | Click on the copy link button             | The image link is copied                 | 




## TDD

To test the app, run this command in the terminal;

`$ python3 manage.py test`


## User Story
* View different photos that interest them.
* Click on a single photo to expand it and also view the details of the photo. 
* Search for different categories of photos. (ie. Travel, Food)
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.

### Technology & Tools
* Python
* Django
* HTML
* CSS
* Bootstrap
* Postgres
* Javascript(jQuery)
* Pip

## Reference

* [Setting up Postgres, SQLAlchemy, and Alembic](https://realpython.com/django-by-example-part-2-postgres-sqlalchemy-and-alembic/)
* [django for Beginners](https://djangoforbeginners.com/introduction/)


## License

MIT License

Copyright (c) 2022 `Kelly Kiiru` 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Authors Contact Details

* [Email](infowithkiiru@gmail.com)
* [LinkedIn](https://www.linkedin.com/in/kiiru-ryan-15a852231/)

