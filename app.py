from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    education_data = [
        {
            "degree": "Bachelor of Technology in CSE",
            "institution": "National Institute of Technology Meghalaya, Sohra",
            "date": "2022 - 2026",
            "gpa": "CGPA: 9.39"
        }
    ]
    
    
    experience_data = [
        {
            "role": "Summer Research Intern (SURAJ)",
            "company": "IIT Jodhpur",
            "date": "June 2025 - July 2025",
            "description": "Analyzed and benchmarked Transformer variants to identify optimal models for low-resource environments, deconstructing architectures to pinpoint computational bottlenecks."
        },
        {
            "role": "Data Science & ML Intern",
            "company": "My Job Grow (Virtual)",
            "date": "Aug 2024 - Oct 2024",
            "description": "Engineered and deployed 3 live ML projects, improving predictive accuracy by 25% using supervised and unsupervised models."
        },
        {
            "role": "AI/ML Coordinator",
            "company": "SanganaKriti - NITM Coding Club",
            "date": "Mar 2024 - Present",
            "description": "Organized and led over 5 ML workshops and AI awareness sessions for more than 100 students to foster a community of AI enthusiasts."
        },
        {
            "role": "Student Convener",
            "company": "NITM Astronomy Club",
            "date": "Aug 2024 - Present",
            "description": "Spearheaded the organization of 3 major club events, successfully increasing student participation by 40%."
        }
    ]
    
    skills_data = {
        "Languages & Databases": [
            {"name": "Python", "proficiency": 95, "usage": 90},
            {"name": "C/C++", "proficiency": 85, "usage": 60},
            {"name": "JavaScript", "proficiency": 80, "usage": 75},
            {"name": "Java", "proficiency": 70, "usage": 40},
            {"name": "SQL (MySQL)", "proficiency": 80, "usage": 50},
            {"name": "NoSQL (MongoDB, Firebase)", "proficiency": 85, "usage": 70},
        ],
        "Frameworks & Libraries": [
            {"name": "TensorFlow & Keras", "proficiency": 90, "usage": 85},
            {"name": "PyTorch", "proficiency": 90, "usage": 85},
            {"name": "Scikit-learn", "proficiency": 95, "usage": 80},
            {"name": "React.js", "proficiency": 80, "usage": 60},
            {"name": "Flask", "proficiency": 85, "usage": 50},
            {"name": "Tailwind CSS", "proficiency": 90, "usage": 75},
        ],
        "Tools & Platforms": [
            {"name": "Git & GitHub", "proficiency": 95, "usage": 100},
            {"name": "Vercel & Netlify", "proficiency": 90, "usage": 80},
            {"name": "Jupyter Notebooks", "proficiency": 95, "usage": 90},
            {"name": "VSCode", "proficiency": 95, "usage": 100},
            {"name": "Streamlit", "proficiency": 80, "usage": 40},
        ]
    }

    project_list = [
        {
            "title": "Nirmaya Health Services",
            "description": "A full-stack, single-page web app to modernize the patient experience and streamline hospital administration, featuring an intelligent AI assistant built with the Google Gemini API.",
            "tech": ["React.js", "Tailwind CSS", "Gemini API", "Firebase Auth"],
            "github": "https://github.com/RSaha0507/Nirmaya-Health-Services",
            "live_link": "https://nirmaya-health-services.netlify.app/",
            "image": "https://placehold.co/600x400/0f172a/amber?text=Nirmaya"
        },
        {
            "title": "Cyber Threat Intelligence System",
            "description": "A Python-based threat analysis platform integrating real-time APIs (AlienVault OTX, AbuseIPDB) and geolocation to analyze and categorize malicious behavior patterns with 92% accuracy.",
            "tech": ["Python", "MongoDB", "Streamlit", "REST APIs"],
            "github": "https://github.com/RSaha0507/Cyber-Threat-Intelligence-and-Response-System",
            "live_link": "#",
            "image": "https://placehold.co/600x400/0f172a/amber?text=CyberThreat"
        },
        {
            "title": "Lightweight Transformer Model",
            "description": "(Ongoing) Developing a lightweight transformer model for resource-constrained devices, implementing optimization methods like pruning and quantization to reduce model size.",
            "tech": ["Python", "PyTorch", "TensorFlow", "Quantization"],
            "github": "https://github.com/RSaha0507/Lightweight-transformer-for-resource-constrained-environment",
            "live_link": "#",
            "image": "https://placehold.co/600x400/0f172a/amber?text=Transformer"
        }
    ]

    awards_list = [
        {"award": "Certificate of Merit", "issuer": "ML Vision 2024"},
        {"award": "GATE 2025 DA Rank 3748", "issuer": "GATE Examination"},
        {"award": "3rd Position, Inter-departmental Hackathon", "issuer": "NIT Meghalaya, 2024"},
        {"award": "Certified in Deep Learning (NPTEL)", "issuer": "Coursera"},
        {"award": "Certificate of Excellence", "issuer": "NITM Astronomy Club"}
    ]

    return render_template(
        "home.html", 
        skills=skills_data,
        experiences=experience_data,
        projects=project_list,
        awards=awards_list
    )

if __name__ == "__main__":
    app.run(debug=True)

