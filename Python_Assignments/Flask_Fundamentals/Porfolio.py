from flask import Flask 
app = Flask(__name__)    
                        
@app.route('/')          
def hello_world():
  return 'Welcome to my porfolio! My name is Chris!' 

@app.route('/projects')          
def show_me_the_cats():
  return '<h1>My Projects:<h1><ul><li>Web Fundamentals<li>Pip<li>Python Fundamentals' 

@app.route('/about')
def about():
    return "I am a Fullstack Developer in training at Coding Dojo. I have many hobbies with my favorite hobby being music. It's not just listening to music but also playing it! I'm a musician myself and I enjoy listening to various bands, and artists in the indie scene. Such bands include my all time favorites, Death Cab For Cutie, Arctic Monkeys, Modest Mouse, The Postal Service, Keaton Henson, Julien Baker, and many more!"


app.run(debug=True)     