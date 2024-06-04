# Coaches Corner

This app is a full stack web app that users (coaches) sign in on, using 
JSON Web Tokens (JWT).

The frontend sends request to backend, and then backend sends response
which there are two tokens (Access and Refresh). The access token will be
generated for a shorter time than refresh token, which is a token that is 
used once the access token has expired.

# Registration and Login pages
The user will be sent to a Register page. Once the user has entered their 
details on that page, the user will then be redirected to a Login page to 
re-enter their details (which have now been saved). 
The user will have access to a database which will show a list of players 
available and players unavailable. However, if the user enters wrong details,
an error will be shown.


