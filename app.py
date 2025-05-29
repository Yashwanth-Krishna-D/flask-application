### Python Flask Application

from flask import Flask, render_template, url_for

app = Flask(__name__)

about_content = ["I'm a third-year B.Tech Computer Science student at Shiv Nadar University, specializing in Artificial Intelligence and Data Science, with a strong focus on Machine Learning, Deep Learning, and Generative AI. My interests lie in building intelligent systems and applying neural networks and large language models to solve real-world problems in areas like computer vision, NLP, and predictive modeling.",

              "I enjoy diving deep into model architectures, fine-tuning pre-trained models, and exploring the latest developments in AI and GenAI. Currently, I’m seeking internship opportunities where I can contribute to impactful projects, collaborate with forward-thinking teams, and continue growing as an AI practitioner.",
                
                "I'm a third-year B.Tech Computer Science student at Shiv Nadar University, specializing in Artificial Intelligence and Data Science, with a strong focus on Machine Learning, Deep Learning, and Generative AI. My interests lie in building intelligent systems and applying neural networks and large language models to solve real-world problems in areas like computer vision, NLP, and predictive modeling.",

                "I enjoy diving deep into model architectures, fine-tuning pre-trained models, and exploring the latest developments in AI and GenAI. Currently, I’m seeking internship opportunities where I can contribute to impactful projects, collaborate with forward-thinking teams, and continue growing as an AI practitioner."]

education_content = {
  "University :": "Shiv Nadar University, Chennai",
  "Degree :": "B.Tech in Artificial Intelligence and Data Science",
  "Batch :": "2023-2027",
  "Grade :": "9.59 CGPA"
}

skills_content = ['Python', 'Flask', 'HTML', 'CSS']

project_content = []

footer_content = "Yashwanth Krishna D. All rights reserved."

@app.route('/')
def homePage():
  return render_template("home.html", about = about_content, education = education_content , footer = footer_content, skills= skills_content)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug= True)