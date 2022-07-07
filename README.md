# Fast API - Boilerplate
Basic FastAPI app with jwt user authentication capability. The app handles user sign up and login and shows an example of how to protect a route to require the token, the add blog post route is protected. The token hash is in the .env file for production use do not keep this in here!


Run the app with:

uvicorn main:app --reload

You will need to create a .env file in the root directory with the following variables set:

secret = [secret_key] #your desired secret key for the hashing algorithm

algorithm = [algorithm] #define the type of hashing algorithm used e.g HS256