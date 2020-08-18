# Flask Facebook chat-bot
Basic Facebook bot to validate a number multiple of 3 or 5 and respond Fizz, Buzz or FizzBuzz according to the value.

### Dtabase
The bot save the facebookid of the sender and all VALID* messages

### Deploy
The bot was deployed on Heroku and you can see it here: https://cloudia-leonardo.herokuapp.com/

### FaceBook
To try the boot you can access it's facebook page: https://www.facebook.com/ChatBot-100714915086229/ and send a menssage.

### Behavior
The bot acceps mensage with a maximum of 280 characters, validate if is a number and responde with fiz and buzz. If e message it's not valid, the the same message will be respod.

### Local Usage
To run the application locally, you need to create an .env file like this:
```
#ACCESS_TOKEN=
#VERIFY_TOKEN=
#
#DB_HOST=localhost
#DB_NAME=fb-message
#DB_PASSWORD=123
#DB_USER=postgres
```
To run the application locally, you can create an temporary database with the command:
```
# make database
```
and run the app:
```
# python app.py
```

### Requests
To try requests to the bot you the requests examples in the collection attached.
I recomend to use Postman.
