from flask import render_template, send_from_directory


def homepage():
    return render_template('homepage.html')


def favicon():
    return send_from_directory('static', 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')
