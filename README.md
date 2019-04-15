# flask-hello-world

Simple "Hello, World" Flask app.

## Installing dependencies.

1. Ensure you've got Python 3 installed. On Mac, `brew install python` should do it, on Debian or its ilk, `apt-get python3` will work.

2. Install `pipenv`. On Mac, the recommended method is `brew install pipenv`. On Debian or Ubuntu, `apt-get install pipenv` should work these days. Other methods are available [here](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv).

3. Run `pipenv install --dev` to get all development dependencies.

## Running the application.

- To launch the app, run `pipenv run flask run -p 5000`. The app can then be connected to on `127.0.0.1:5000`.

- To enable more detailed logging, run the app with the `FLASK_LOG_LEVEL` environment variable set to `DEBUG`, like so: `FLASK_LOG_LEVEL=DEBUG pipenv run flask run -p 5000`. This will add log messages for every request.

- To enable a full debugging environment, run the app with `FLASK_ENV` set to development, like so: `FLASK_LOG_LEVEL=DEBUG FLASK_ENV=development pipenv run flask run -p 5000`. This will also enable a debug shell on error.

## Testing

1. You can exercise the app from the command line using `curl`. A few examples:

    ```
    $ curl http://127.0.0.1:5000/
    <p>Hello, World</p>
    
    $ curl -H "Accept: application/json" http://127.0.0.1:5000/
    {"message":"Good morning"}

    $ curl -X POST http://127.0.0.1:5000/
    <p>Hello, World</p>

    $ curl -X POST -H "Accept: application/json" http://127.0.0.1:5000/
    <p>Hello, World</p>
    ```

2. You can run some simple mocked tests by running `pipenv run pytest`, analogous to the `curl` commands above.
