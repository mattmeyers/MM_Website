from flask import Flask, render_template, url_for
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/euler')
def euler():
    return render_template('euler.html')

@app.route('/math')
def math():
    return render_template('math.html')

@app.route('/euler/<string:pe>')
def eulerPE1(pe):
    return render_template(f'ProjectEuler/{pe}/{pe}.html')


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
