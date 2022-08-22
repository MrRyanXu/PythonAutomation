"""


"""
from flask import Flask,request
from jinja2 import Template

app = Flask(__name__)
@app.route("/")
def index():
    name = request.args.get('name', 'admin')
    t = Template("HEllo " + name)
    return t.render()

    # 修复
    # t = Template("HEllo {{n}}")
    # return t.render(n = name)
@app.route("/delete")
def delete():
    pass
    return "删除成功！"

if __name__ == '__main__':
    app.run(debug=True)


