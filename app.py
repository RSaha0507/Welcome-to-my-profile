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
    project_list = [
        {
            "title": "AI Chatbot",
            "description": "A chatbot that responds to user queries using NLP.",
            "tech": "Python, Flask, OpenAI API",
            "github": "https://github.com/yourusername/ai-chatbot"
        },
        {
            "title": "Web Scraper",
            "description": "Scraped news headlines and stored them in a CSV.",
            "tech": "Python, BeautifulSoup",
            "github": "https://github.com/yourusername/web-scraper"
        },
        {
            "title": "Portfolio Website",
            "description": "This personal portfolio site built with Flask.",
            "tech": "Python, Flask, HTML/CSS",
            "github": "https://github.com/yourusername/portfolio-site"
        }
    ]
    return render_template("projects.html", projects=project_list)


# Contact page route (optional)
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
