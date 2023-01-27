# Example Application - Complimentr

This application was built using a tutorial from  [Introduction to APIs course](https://www.youtube.com/watch?v=GZvSYJDk-us&t=5527s).

>  I used [glitch](https://glitch.com/) to test and deploy the application . 



## Local Installation

Copy `.env.example` to `.env` and update it with your [Twilio](https://twilio.com) credentials by running this command 
`cp .env.example .env`

Check how to secure your [twilio credentials](https://www.twilio.com/docs/usage/secure-credentials)

### Running the application

* `python -m venv .venv`
* `source ./.venv/bin/activate`
* `pip install -r requirements.txt`
* `FLASK_ENV=development flask run`

#### In Development mode

* Run [ngrok](https://ngrok.com/) on port 5000
* Visit your ngrok url!
