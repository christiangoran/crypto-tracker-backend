# BlockBoard Cryptocurrency Tracker

## Bugs & problems

- Hitting the 32kb limit on Heroku config vars

  - When trying to add a config var with the coinmarketcap API, I am unable to, and the most probable cause for it is that I have reached the 32kb limit that Heroku has on config vars.
    - Solution: There seem to have been a corrupted Heroku app, after deleting and creating a new app, I could add the necessary config vars

- After deploying to Heroku, my currency model was empty and I need to find out how to make my Heroku app call the Coinmarketcap API to populate my currency model.

  - I added the Heroku Scheduler service to my Heroku app and configured it to run "python3 manage.py update_currencies" every 10 minutes.

- When sending a request from my signup form, a new user was registered to the database, but somewhere in the execution order after the registration I get a 500 error response. After looking through Heroku logs and not finding anything but a 500 error. I added LOGGING to my Django settings.py.
  - Solution: After 4-5 hours of searching for what the error could be. What eventually appeared to be the problem was the use of useNavigate/useHistory and that the use of this changed with the latest version of React. So after changing the code snippet "history.push("/signin");" and "const history = useNavigate();" to "const navigate = useNavigate();" and "navigate("/signin")" I managed to finally make it work.

LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'handlers': {
'console': {
'class': 'logging.StreamHandler',
},
},
'loggers': {
'django': {
'handlers': ['console'],
'level': 'DEBUG',
'propagate': True,
},
},
}

- The problem was then identified as being a missing Meta.model in my CurrentUserSerializer

###

Cloudinary storage
Rest
Pillow

Sources:

https://stackoverflow.com/questions/69510138/how-to-get-data-from-external-api-to-django-rest-framework - for connecting external API to Rest

https://medium.com/@chilinski.a/how-to-seed-a-django-api-with-data-from-an-external-api-b577b6e6ad54 - connecting external API to Rest

https://www.youtube.com/watch?v=QA6oTpMZp84 - using Coingeckos API

https://www.datacamp.com/tutorial/making-http-requests-in-python - Making a http request in Python

https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/ - custom management commands

https://www.youtube.com/watch?v=f3GfkvfpVAE - learning how to use coinmarketcaps api

https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide - how to use their api
