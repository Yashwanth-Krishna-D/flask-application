### Python Flask Application

from flask import Flask, render_template

app = Flask(__name__)

about_content = ["I'm a third-year B.Tech Computer Science student at Shiv Nadar University, specializing in Artificial Intelligence and Data Science. My academic journey and hands-on experience revolve around Machine Learning, Deep Learning, and Generative AI, with a strong interest in applying neural networks and large language models to real-world challenges in areas like computer vision, NLP, and predictive analytics.",

"While my primary focus lies in intelligent systems and advanced AI, I also have solid experience in full-stack web development. I believe being deeply invested in ML doesn’t mean neglecting core software and web development skills—both complement each other in building robust, deployable AI solutions. I enjoy exploring model architectures, fine-tuning pre-trained models, and staying engaged with the latest in AI and GenAI.",

" I'm currently seeking internship opportunities where I can contribute to impactful projects, work with innovative teams, and continue growing as a well-rounded AI practitioner.",
                 
"Beyond academics, I enjoy contributing to open-source projects and experimenting with real-time data applications. I'm also comfortable working in both collaborative and independent settings. With every project, I strive to bridge the gap between theory and practical deployment. I aim to be part of teams that value curiosity, creativity, and meaningful impact through technology."]

education_content = {
  "University :": "Shiv Nadar University, Chennai",
  "Degree :": "B.Tech in Artificial Intelligence and Data Science",
  "Batch :": "2023-2027",
  "Grade :": "9.59 CGPA"
}

skills_content = [
    "Python (Programming Language)",
    "Machine Learning",
    "Multimodal Affective Analysis",
    "Affective Computing",
    "Exploratory Data Analysis",
    "Feature Engineering",
    "Statistical Modeling",
    "Probability",
    "Statistics",
    "Data Visualization",
    "Machine Learning with Python",
    "Data Visualization with Python",
    "Flask",
    "SQLAlchemy",
    "SQLite",
    "RESTful APIs",
    "Beautiful Soup",
    "Object-Oriented Programming (OOP)",
    "Tableau",
    "JavaScript",
    "Responsive Web Design",
    "Cascading Style Sheets (CSS)",
    "HTML",
    "Java",
    "C++",
    "C (Programming Language)"
]


project_content = []

footer_content = "Yashwanth Krishna D. All rights reserved."

@app.route('/')
def homePage():
  return render_template("home.html", about = about_content, education = education_content , footer = footer_content, skills= skills_content)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug= True)