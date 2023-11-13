# this file runs the app and render the html page

# import necessary modules
from flask import render_template
from tools import app




# define the route
@app.route('/')
def index_html():
    return render_template('index.html')


# Run the app
if __name__ == '__main__':
    app.run(port=5001, debug=True)
