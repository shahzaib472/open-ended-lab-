from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- 1. Home Page Pathway ---
@app.route('/')
def home():
    return render_template('home.html')

# --- 2. About Page Pathway ---
@app.route('/about')
def about():
    return render_template('about.html')

# --- 3. Services Page Pathway ---
@app.route('/services')
def services():
    return render_template('services.html')

# --- 4. Gallery Page Pathway ---
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# --- 5. Contact Form Submission Pathway ---
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        print(f"[SERVER TRACE] Incoming form message from contact: {name}")
        return redirect(url_for('home'))
    return render_template('contact.html')

# --- 6. Simulated Login Pathway ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        print(f"[SERVER TRACE] User login attempt capture: {username}")
        return redirect(url_for('home'))
    return render_template('login.html')

# --- 7. Simulated Registration Pathway ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        print(f"[SERVER TRACE] User registration register action: {username}")
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1011)
