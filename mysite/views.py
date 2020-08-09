from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Product

# Create your views here.
def about(request):
    html = '''
<html>
<head>
<title>About Myself</title>
</head>
<body>
<h2>Justin Wu</h2>
<hr>
<p>
Hi! I'm Justin Wu,  Nice to meet you.
</p>
</body>
</html>
'''

    return HttpResponse(html)


def listing(request):
    html = '''
<html>
<head>
<title>商品列表</title>
</head>
<body>
<h2>商品列表</h2>
<hr>
<table width=400 border=1 bgcolor='#ccffcc'>
{}
</table>
</body>
</html>
'''
    Products = Product.objects.all()
    tags = '<tr><td>品名</td><td>售價</td><td>庫存量</td></tr>'
    for p in Products:
        tags = tags + '<tr><td>{}</td>'.format(p.name)
        tags = tags + '<td>{}</td>'.format(p.price)
        tags = tags + '<td>{}</td></tr>'.format(p.qty)

    return HttpResponse(html.format(tags))