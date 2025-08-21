from flask import Flask, render_template

app = Flask(__name__)

# Home page route
@app.route("/")
def home():
    return render_template("home.html")

# About page route
@app.route("/about")
def about():
    return render_template("about.html")

# Projects page route
@app.route("/projects")
def projects():
    # This list is now based on your resume
    project_list = [
        {
            "title": "Nirmaya Health Services",
            "description": "A full-stack, single-page web app to modernize the patient experience and streamline hospital administration.",
            "tech": ["React.js", "Tailwind CSS", "Gemini API", "Firebase"],
            "github": "https://github.com/RSaha0507/Nirmaya-Health-Services", # Assumed link, please update
            "live_link": "https://nirmayahealthservices.netlify.app" # Add your live project link here
        },
        {
            "title": "Cyber Threat Intelligence System",
            "description": "A Python-based threat analysis platform integrating real-time APIs from AlienVault OTX and AbuseIPDB.",
            "tech": ["Python", "MongoDB", "Streamlit", "REST APIs"],
            "github": "https://github.com/RSaha0507/Cyber-Threat-System", # Assumed link, please update
        },
        {
            "title": "Lightweight Transformer Model",
            "description": "(Ongoing) Developing a lightweight transformer model for deployment on resource-constrained devices.",
            "tech": ["Python", "PyTorch", "Pruning", "Quantization"],
            "github": "https://github.com/RSaha0507/Lightweight-Transformer", # Assumed link, please update
        }
    ]
    # We pass the list of projects to the projects template
    return render_template("projects.html", projects=project_list)

# Contact page route
@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
