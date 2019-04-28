from flask import Flask
import argparse

def main():
    args = parse_args()
    app = create_app(path=args.path)
    run_app = app.run(host='0.0.0.0', port=args.port)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', action='store', dest='port', default='8080')
    parser.add_argument('--path', action='store', dest='path', default='/healthcheck')

    args = parser.parse_args()
    return args

def create_app(path):
    """
    Create the Flask app and the provided route
    param: path; The path of the healthcheck.  Must start with a leading '/'

    returne: app; A Flask app with the desired route
    """

    app = Flask(__name__)

    @app.route(path)
    def healthcheck():
        return "OK"

    return app

if __name__ == '__main__':
    main()