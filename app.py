from flask import Flask, render_template, request, redirect, url_for, session, flash, make_response
from flask_minify import minify, decorators
from datetime import datetime

app = Flask(__name__)

app.secret_key = "cjn330e3i0eueid9320"

minify(app=app, html=True, js=True, cssless=True)



elements = ['', 'articles', 'articles/quantum-computers', 'articles/quantum-computers',
            'articles/quantum-mechanics', 'articles/what-is-antimatter',
            'articles/time-travel-restrictions-on-changing-past', 'articles/time-paradoxes', 'articles/egypt-pyramids',
            'articles/time-slip-1', 'articles/time-slip-2', 'articles/time-slip-3', 'articles/time-slip-4',
            'articles/theory-of-relativity', 'articles/dark-matter-dark-energy',
            'articles/Bermuda-and-Dragon"s-triangle', 'articles/mandela-effect', 'articles/time-travel-possible-or-not',
            'articles/big-bang-theory','articles/mass-and-relativity','articles/wormholes']


@app.route("/", methods=['POST', 'GET'])

def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        name = request.form.get('username')
        email = request.form.get('email')
        message = request.form.get('message')
        if (name != "" and email != "" and message != ""):
            fmessage = {
                "name":name,
                "email":email,
                "message":message
            }
            f = open("message.txt", "a")
            f.write(f"{fmessage}\n\n")
            f.close()
            # entry = Contacts(usrname=name, email=email, message=message, date_time=datetime.now())
            # db.session.add(entry)
            # db.session.commit()
        return render_template('index.html')


@app.route("/articles")
def articles():
    return render_template('blog.html')


@app.errorhandler(404)
def route1(e):
    return render_template('noroute.html')


@app.route("/articles/quantum-computers")
def post1():
    return render_template('quantum-computers.html')


@app.route('/articles/quantum-mechanics')
def post2():
    return render_template('quantum-mechanics.html')


@app.route('/articles/Heisenberg-Uncertainty-Principle')
def post3():
    return render_template('uncertainty.html')


@app.route('/articles/what-is-antimatter')
def post4():
    return render_template('antimatter.html')


@app.route('/articles/time-travel-restrictions-on-changing-past')
def post5():
    return render_template('time-travel-past.html')


@app.route("/articles/time-paradoxes")
def post6():
    return render_template("time-paradoxes.html")


@app.route('/articles/egypt-pyramids')
def post7():
    return render_template('egypt-pyramids.html')


@app.route('/articles/time-slip-1')
def post8():
    return render_template('time-slip-1.html')


@app.route('/articles/time-slip-2')

def post9():
    return render_template('time-slip-2.html')


@app.route('/articles/time-slip-3')
def post10():
    return render_template('time-slip-3.html')


@app.route('/articles/time-slip-4')
def post11():
    return render_template('time-slip-4.html')


@app.route('/articles/theory-of-relativity')
def post12():
    return render_template('theory-of-relativity.html')


@app.route('/articles/dark-matter-dark-energy')
def post13():
    return render_template('dark-matter.html')


@app.route('/articles/Bermuda-and-Dragon"s-triangle')
def post14():
    return render_template(('mysterious-triangles.html'))


@app.route('/articles/mandela-effect')
def post15():
    return render_template('mandela-effect.html')


@app.route('/articles/time-travel-possible-or-not')
def post16():
    return render_template('time-travel-possible.html')


@app.route('/articles/big-bang-theory')
def post17():
    return render_template('big-bang-theory.html')
    
@app.route('/articles/mass-and-relativity')
def post18():
    return render_template('mass-relativity.html')

@app.route('/articles/wormholes')
def post19():
    return render_template('wormholes.html')

@app.route('/articles/black-holes')
def post20():
    return render_template('black-hole.html')

@app.route('/articles/spacetime')
def post21():
    return render_template('spacetime.html')

@app.route('/articles/information-paradox')
def post22():
    return render_template('information-paradox.html')

@app.route('/articles/bootstrap-paradox')
def post23():
    return render_template('bootstrap-paradox.html')

@app.route('/robots.txt')
def info():
    return render_template('robots.txt')

@app.route("/sitemap.xml")
def sitemap_xml():
    response= make_response(render_template("sitemap.xml"))
    response.headers['Content-Type'] = 'application/xml'
    return response


if __name__ == "__main__":
    app.run(debug=True)
