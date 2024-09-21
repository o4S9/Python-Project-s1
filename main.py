from flask import Flask, render_template, request,url_for
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt


app = Flask(__name__)




  


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/login',methods = ['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')
    

@app.route('/sign_up',methods = ['GET','POST'])
def signup():
    data = request.form
    print(data)
    # if request.method == 'POST':
    #     email = request.form.get('email')
    #     firstName = request.form.get('firstName')
    #     password1= request.form.get('password')
    #     password2 = request.form.get('password1')
    
    #     if len(email)=="onkarsutar4939@gmail.com":
    #         print(email)
    #     elif len(firstName)=="Onkar":
    #         print(firstName)

    #     elif password1 == password2:
    #         print(password1,password2)

    #     elif len(password1) == "1234":
    #         print(password1)
        # elif email =="Onkar" or password1 == "4939":
        #     print(email,firstName,password1)
        # else:
        #     render_template('home.html')

            #add user database
            

    return render_template('sign_up.html')


   
@app.route('/home')
def home():
    return render_template('home.html')






if __name__ == "__main__":
    app.run(debug=True)