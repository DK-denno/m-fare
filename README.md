# M-FARE
This is an application that allows long distance travellers to book bus tickets using their cellphones, 
Once the transaction has been made the saccos are able to view the the payments and a conformation message is sent to the user.
## Built by: 
#EUGENE NZIOKI
#Kwesi Makonnen
#Dennis Kamau
#Aurelia Naiyoma

## User/Sacco  Requirements
 1. User, should be able to choose my destination.
 2. User, should view the sacco's location.
 3. User, should be able to book a ticket.
 4. User, should make payment to sacco.
 5. User, should receive a message that payment has been made and a ticket has been booked.
 5. Sacco, should view user transactions.
 6. Sacco , should to select the routes that my matatu will take.
 8. Sacco should view all payments made to it.
 9. Sacco should be able to send messages to its passengers/riders.

## Features

  + [x] Functioning authentication system
  + [x] Implementation of one-many and many - many relationships.
  + [x] project  has a user model.
  + [x] project  has a sacco model.
  + [x] project  has a admin  model.
  + [x] project  has a fares  model.
  + [x] sacco dashboard
  + [ ] Admin dashboard 
  + [ ] Payment transactions between user(rider), admin and sacco
  + [x] user receiving confirmation message from sacco 

## Installation

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.

* Tested on Debian Linux
* Python 3.6.4

## Cloning of the respository
   * In terminal:
   
    $ git clone https://github.com/DK-denno/m-fare.git
    
## Creating the Virtual Environment

    sudo apt-get install python3.6-venv
    python3.6 -m venv virtual
    source virtual/bin/activate

## Install Dependencies

    pip3 install -r requirements.txt
    
## Required Libraries     
   * Flask==0.12.2
   * Flask-Bootstrap4==4.0.2
   * Flask-Script==2.0.6
   * gunicorn==19.7.1
   * material kit
   
## Running Tests

    python3.6 manage.py test
    
## Running the web app 
    python3.6 manage.py server
   
   open app in browser by default on 127.0.0.1:5000

## Live Demo

This web app can be accessed from the following link:

    https://m-fare.herokuapp.com/ 
    
## Quick Start

    usage: manage.py [-?] {server,test,shell,runserver} ...

    positional arguments:
      {server,test,shell,runserver}
        server              Runs the Flask development server i.e. app.run()
        test                Run the unit tests.
        shell               Runs a Python shell inside Flask application context.
        runserver           Runs the Flask development server i.e. app.run()
    
    optional arguments:
      -?, --help            show this help message and exit
      
## Technology Used

   * Python3.6
   * Flask   
   * Heroku
   
## License Information

   MIT License

Copyright(c) 2018

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



Collapse 

Message Input

Message Eugene Nzioki, Kwesi Makonnen, Naiyoma Aurelia