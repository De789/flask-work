from flask import Flask,redirect,url_for,request,render_template,make_response
from markupsafe import escape
app=Flask(__name__)



@app.route("/")
def hello_world():
    return "hello world"


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    return render_template('login.html')
 

@app.route('/success/<name>')
def success(name):
    return f"Welcome, {name}!"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/user/<int:id>')
def show_user_id(id):
    # show the user profile for that user
    return f'User {escape(id)}'

@app.errorhandler(404)
def not_found(error):
    res=make_response(render_template('error.html'),404)
    res.headers['X-headers']='Something '
    return res


if __name__=="__main__":
    app.run(debug=True)

