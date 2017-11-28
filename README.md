# xanadu
Xan·a·du ˈzanəˌdo͞o/ noun an idealized place of great or idyllic magnificence and beauty.

Having said that, this application, is a bucket list that let's you keep a list of those idealized places that you would love to visit but not just limited to geographical places but also a list of things that you would love to have done or experiences you would have wanted before you know, you kick it!

## Getting Started
___

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

This application has been tested and run using `python 3 ` and you can download it from their official page [here](https://python.org/downloads/).

I did all my development from a virtual environment and this [documentation](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
gives a detailed methodology to create and use a virtual environment.

### Prerequisites
___

Together with the documentation of the application I have included a [requirements.txt](requirements.txt) file
which has a list of the modules that the application depends on to run.

### Installing
___

Create a virtual environment. I called mine `xanadu` and had it running on python 3.

Xanadu uses postgres by default and you have to create a postgres database and set the database as follows:

*Anything between the angle brackets you have to replace with your settings*

    SQLALCHEMY_DATABASE_URI = postgres://<user>:<password>@<host>:<port>/<database_name>

If you don't want to use postgres just leave the settings as they are and the app will create an sqlite database for you.

Find the instructions for installing and using a virtual environment and virtualenv wrapper [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Run the environment using `workon xanadu` and clone my application by running the following command on your terminal:

   `git clone https://github.com/Gathondu/xanadu.git`

## Running the tests
___

Explain how to run the automated tests for this system
