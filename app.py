import flask, flask.views
from flask import request,redirect
import os
app = flask.Flask(__name__)

#app = Flask(static_folder='static')

def path():
    arr = []
    for dirName, subdirList, fileList in os.walk('./static/Experiment'):
        temp = ''
        for fname in fileList:
            #path = '%s/%s'%(dirName,fname)
            if 'test' not in dirName:
                if dirName == temp:
                    continue
                d = {}
                x = dirName.split('/')[-1][6:]
                
                d['test_img_path'] = 'static/Experiment/test/%s%%20(%s).jpg'%(x[0],x[1:])
                arr2 = []
                for dirName2, subdirList2, fileList2 in os.walk(dirName):
                    arr2 = [dirName +'/'+ i for i in fileList2]
                d['result_img_path'] = arr2
                arr.append(d)
                temp = dirName
    return arr

@app.route('/<page>')
def main(page):
    if not page:
        self.redirect('/1')
    data = path()
    page = int(page)-1
    return flask.render_template('index.html',data=data,page=page)

@app.route('/')
def foo():
    return redirect("/1")

if __name__ == '__main__':
    #path()
    app.debug = True
    app.run(host='0.0.0.0',port=5003)
