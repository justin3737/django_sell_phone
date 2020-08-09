from django.shortcuts import render
from django.http import HttpResponse

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