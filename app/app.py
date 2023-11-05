from jinja2 import Environment, FileSystemLoader
from post_infos import get_publication_infos

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

# render publications.html with layout publications.html
template = env.get_template('publications.html')
publication_infos = get_publication_infos()
with open('publications.html', 'wb') as f:
    f.write(template.render(headerimg='/assets/img/covers/maincover.jpg',
                            sections=publication_infos).encode('utf-8'))

# render research.html with layout research.html
template = env.get_template('research.html')
with open('research.html', 'wb') as f:
    f.write(template.render(headerimg='/assets/img/covers/maincover.jpg').encode('utf-8'))
