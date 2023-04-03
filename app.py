#從flask包導入flask類
from flask import Flask 
from flask import url_for
# 透過實例化這個類，創建一個對象app
app = Flask(__name__)

#註冊處理函數，可以理解為請求處理函數
@app.route('/index') #一个视图函数也可以绑定多个 URL，这通过附加多个装饰器实现
@app.route('/home')
def hello(): 
    return '<h1>Hello 龍貓!</h1><img src="http://helloflask.com/totoro.gif">'
# 为了便于理解，你可以把 Web 程序看作是一堆这样的视图函数的集合
# 编写不同的函数处理对应 URL 的请求。

from markupsafe import escape
# 我们也可以在 URL 里定义变量部分。
# 比如下面这个视图函数会处理所有类似 /user/<name> 的请求
@app.route('/user/<name>')
# 不论你访问 http://localhost:5000/user/greyli
# 还是 http://localhost:5000/user/peter
# 都會觸發這個函數，觸發點是user
def user_page(name):
    return f'User: {escape(name)}' #我们也可以在视图函数里获取到这个变量值

#注意 用户输入的数据会包含恶意代码，所以不能直接作为响应返回
# 需要使用 MarkupSafe（Flask 的依赖之一）提供的 escape() 函数对 name 变量进行转义处理
# 比如把 < 转换成 &lt;。这样在返回响应时浏览器就不会把它们当做代码执行。

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请访问 http://localhost:5000/test 后在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 生成 hello 视图函数对应的 URL，将会输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'

#定義虛擬數據
data_name = 'Grey Li'
data_movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

from flask import render_template

@app.route('/')
def index():
    # 在传入 render_template() 函数的关键字参数中，左边的 movies 是模板中使用的变量名称
    # 右边的 movies 则是该变量指向的实际对象。这里传入模板的 name 是字符串，movies 是列表
    # 但能够在模板里使用的不只这两种 Python 数据结构，你也可以传入元组、字典、函数等。
    return render_template('index.html', name=data_name, movies=data_movies)