from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template,Context

# Create your views here.
def test_html(request):
    return render(request,'test.html',{'name':'价值投资学习网'})


def test_another(request):
    a = {}
    a['name'] = '价值投资学习网'
    a['course'] = ['大咖介绍', '入门知识', '实战案例', '经典书籍']
    a['add'] = {'name': '价值投资学习网', 'address': 'www.jiazhi.com'}
    a['test_hello'] = test_hello
    a['class_obj'] = Website()

    return render(request,'test_another.html',a)

def test_hello():
    return '欢迎来到价值投资学习网,函数'

class Website:
    def Website(self):
        return '欢迎来到价值投资学习网,类实例'

def hello_web(request):
    #调用template()方法生成模板,这种写法还不把人写死啊尼玛
    t = Template(
        '''
        {% if web.name == '价值投资网' %}
            {% if printable %}
                <h1> Hello 价值投资网 <h1>
            {% else %}
                <h2> 欢迎下次光临 <h2>
            {% endif %}
        {% endif %}
        '''
    )
    #使用Context来装参数
    c = Context({'web':{'name':'价值投资网'},'printable':False})
    #用render方法来把参数传入给html
    html = t.render(c)

    return HttpResponse(html)

def test_url(request):
    return render(request,'test.url')
