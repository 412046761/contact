from flask import Flask,render_template,request
import datetime

app = Flask(__name__)


@app.route('/test')
def hello_world():
    return 'Hello World11111!'

# get 字符串传参
@app.route('/user/<name>')
def hello(name):
    return 'Hello,%s'%name

# get 数字传参                 此外，还有float类型
@app.route('/user/<int:id>')
def hello1(id):
    return 'Hello,%d号会员！'%id

#路由路径不能重复。用户通过唯一路径访问特定的函数

# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/")
def index2():
    time = datetime.date.today()  # 普通变量
    name = ["张三","李四","王五"]   # 列表类型
    task = {"任务":"打扫卫生","任务2":"打扫卫生2","任务3":"打扫卫生3"}
    return render_template("index.html",var = time,list = name,task = task)

# 表单提交
@app.route("/test/register")
def register():
    return render_template("test/register.html")

# 表单接受
@app.route('/result',methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        # 表单提交的内容
        rs = request.form
        return render_template("test/result.html",rs = rs)

if __name__ == '__main__':
    app.run()
