from flask import Flask,redirect,url_for,request,render_template

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



if __name__=="__main__":
    app.run(debug=True)

