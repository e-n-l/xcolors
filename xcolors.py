# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template
from glob import glob

app = Flask(__name__)

@app.route('/')
def index():
    directory = os.path.dirname(__file__)
    path = os.path.join(directory, 'templates', 'xcolors')
    themes = ['xcolors/%s'%os.path.basename(t) for t in glob('./{0}/*.html'.format(path))]
    return render_template('index.html', themes=themes)

if __name__ == '__main__':
    from xcolor.generator import Generator
    path = os.path.dirname(__file__)
    xcolor = Generator(os.path.join(path, 'color_files'),
                       os.path.join(path, 'templates', 'xcolors'))
    xcolor.generate_files()

    port = int(os.environ.get('PORT', 8080))
    debug = os.environ.get('DEBUG') in ("true", "True")

    app.run(port=port, debug=debug)