from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for services/commodities (used in home.html and services.html)
services = [
    {"title": "Ferrous", "desc": "Shredded steel, HMS, bushling, PNS, cast iron & rail scrap."},
    {"title": "Non-Ferrous", "desc": "Zurik, cables, UBC, bottlecaps, foils, Tense, TT, Telic, wheels, shredded Al, zinc products."},
    {"title": "Semi-Finished", "desc": "Billets, slabs, HR coils, CR sheets & wire rods."},
    {"title": "Waste Paper", "desc": "OCC, SOP, newsprint, magazines & mixed grades."},
    {"title": "Plastics", "desc": "PET, HDPE, PP, LDPE & PVC recycling grades."},
]

@app.route('/')
def home():
    return render_template('home.html', services=services)

@app.route('/services')
def services_page():
    return render_template('services.html', services=services)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # For now just print to console - you can add email sending later
        print(f"Contact from {name} ({email}): {message}")
        return render_template('contact.html', success=True)
    return render_template('contact.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
