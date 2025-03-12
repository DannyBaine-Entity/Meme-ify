from flask import render_template, request
from app import app

# Landing page
@app.route('/')
def landing():
    return render_template('landing.html')

# Login page
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Handle login logic
        return 'Login successful'
    return render_template('login.html')

# Sign up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle signup logic
        return 'Signup successful'
    return render_template('signup.html')

# Meme page
@app.route('/meme')
def meme():
    # Retrieve and display memes
    return render_template('meme.html')

# Favorite memes page
@app.route('/fav')
def favorite():
    # Retrieve and display favorite memes
    return render_template('favorite.html')

# Profile page
@app.route('/profile')
def profile():
    # Retrieve and display user profile information
    return render_template('profile.html')

# Create meme page
@app.route('/create-meme', methods=['GET', 'POST'])
def create_meme():
    if request.method == 'POST':
        # Handle meme creation logic
        return 'Meme created successfully'
    return render_template('create_meme.html')
