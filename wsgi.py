from app import app

if __name__ == '__main__':
    app.run()

# This line is needed for Gunicorn
application = app