from flask import Flask, render_template

app = Flask(__name__)

# Global services data – available to any route that needs it
services = [
    {
        "title": "Non-Ferrous",
        "desc": "High-quality non-ferrous recyclables including aluminium, copper, zinc, nickel, lead, tin and alloys. Corrosion-resistant and conductive materials essential for electronics, automotive, aerospace, renewable energy and more. We supply consistent grades with full traceability.",
        "image": "non-ferrous.jpg"
    },
    {
        "title": "Ferrous",
        "desc": "Premium ferrous metals and scrap including various grades of steel, stainless steel, cast iron and other iron-based materials. Key inputs for construction, infrastructure, automotive and heavy industry. Strict quality sorting and processing standards applied.",
        "image": "ferrous.jpg"
    },
    {
        "title": "Semi-Finished Products",
        "desc": "Intermediate steel and metal products such as billets, blooms, slabs, hot-rolled coils, cold-rolled sheets and other cast or rolled forms ready for further processing into finished goods. Delivered with precise dimensional tolerances and chemistry control.",
        "image": "semi-finished.jpg"
    },
    {
        "title": "Waste Paper",
        "desc": "Recovered paper grades including OCC (old corrugated containers), sorted office paper, newsprint, magazines, mixed paper and other recovered fibre sources. Used by paper mills for sustainable packaging, tissue and printing production.",
        "image": "waste-paper.jpg"
    },
    {
        "title": "Plastics",
        "desc": "Post-consumer and post-industrial recyclable plastics including PET, HDPE, PP, LDPE, PVC and other common polymers. Sourced, sorted, baled and supplied to reprocessors, compounders and manufacturers supporting circular economy goals.",
        "image": "plastics.jpg"
    }
]

@app.route('/')
def home():
    return render_template('home.html', services=services)  # ← This line fixes the homepage error

@app.route('/services')
def services_page():  # Renamed to prevent name clash with the list
    return render_template('services.html', services=services)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/book')
def book():
    return render_template('book.html')

if __name__ == '__main__':
    app.run()
