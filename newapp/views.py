from django.shortcuts import render

# Create your views here.
def test_html(request):
    return render(request,'test.html',{'name':'价值投资学习网'})
