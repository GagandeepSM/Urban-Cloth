  
from flask import render_template, url_for, flash, redirect, request
from urbancloth import app, db, bcrypt
from urbancloth.forms import RegistrationForm, LoginForm, BagForm
from urbancloth.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'brand' : 'H&M',
        'product_name' : 'Men Olive Green Solid Cotton T-shirt Regular Fit',
        'price' : '£70'
    },

    {
        'brand' : 'Adidas',
        'product_name' : 'Men Maroon Solid T-shirt Regular Fit',
        'price' : '£80' 
    },

    {
        'brand' : 'Nike',
        'product_name' : 'Men Blue Solid T-shirt Sports Fit',
        'price' : '£90' 
    }
]

women = [
    {
        'brand' : 'H&M',
        'product_name' : 'women Olive Green Solid Cotton T-shirt Regular Fit',
        'price' : '70'
    },

    {
        'brand' : 'Adidas',
        'product_name' : 'Women Maroon Solid T-shirt Regular Fit',
        'price' : '80' 
    },

    {
        'brand' : 'Nike',
        'product_name' : 'Women Blue Solid T-shirt Sports Fit',
        'price' : '90' 
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts )

@app.route("/men")
def men():
    return render_template('men.html', posts = posts)

@app.route('/women')
def women():
    return  render_template('women.html')   

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/wishlist')
@login_required
def wishlist():
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('wishlist.html', image_file=image_file)

@app.route('/bag')
@login_required
def bag():
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('bag.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()       
        flash('Your Account has been created you can now log in' , 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/bag/items", methods=['GET', 'POST'])
@login_required
def bag_items():
    form = BagForm()
    if form.validate_on_submit():
        flash('Your item has been added to bag', 'success')        
    return render_template(url_for('bag', form=form))