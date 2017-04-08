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

    SQLALCHEMY_DATABASE_URI = postgres://postgres:<password><host>:<port>/<database_name>

If you don't want to use postgres just leave the settings as they are and the app will create an sqlite database for you.

Find the instructions for installing and using a virtual environment and virtualenv wrapper [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Run the environment using `workon xanadu` and clone my application by running the following command on your terminal:

   `git clone https://github.com/Gathondu/xanadu.git`

## Running the tests
___

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
