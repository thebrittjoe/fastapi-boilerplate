# Fast API - Boilerplate
Basic FlaskAPI app with jwt user authentication capability. The app handles user sign up and login and shows an example of how to protect a route to require the token, the add blog post route is protected. The token hash is in the .env file for production use do not keep this in here!


Run the app with:

uvicorn main:app --reload