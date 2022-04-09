from jinja2 import Environment, FileSystemLoader
import os

# load layout folder
env = Environment(loader=FileSystemLoader(['layout', '.']))

# render 404.html
template = env.get_template('404.html')
with open('404.html', 'w') as f:
    f.write(template.render())

# render index.html
template = env.get_template('index.html')
with open('index.html', 'w') as f:
    f.write(template.render())
