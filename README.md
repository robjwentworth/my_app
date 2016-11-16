# my_app
MVP of Capstone Project. Code runs on Amazon EC2 

URL: http://ec2-35-162-239-114.us-west-2.compute.amazonaws.com:5000

This project utilizes a TdidfVectorizer to vectorize a large series of the body of articles for feature data.
Said feature data is then fit to a Mulitnominal Naive Bayes model. The app takes any text the user sends it and then
predicts a section name and sent back to the html page.

The application itself is simplistic. However, the primary purpose was to run this application on the web for everyone
via Amazon Web Services (aws). The initial purpose was to utilize Amazon ElasticBeanstalk for the deployment process.
For simple flask applications this is easy to utilize and deloy. (As long as your application for python is named
application.py) 

However, utilizing the deploy for some of the more complex pieces of the project such as Sci-Kit Learn, provided to be more
difficult that initially imagined. I learned a great deal about the inner workings of aws though this challenge. It is possible to use BeanStalk to do the deployment, however I risked not getting anything out in time. I was able to deploy the code with BeanStalk to an Amazon Linux EC2 instance. I then installed numpy, scipy and sklearn packages to the instance. I figured it would now work. However...that was not the case as it did not recognize the new packages. I then was able to run the application successfully off of the EC2 instance itself. It will run day and night until I decide to shut it off.

The port number prohibits me from running Route 53 from AWS to give the website a great name. This was a secondary goal of the project. This MVP will run just in case any future work proves too difficult or does not bear meaningful fruit.


