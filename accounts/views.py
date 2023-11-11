from django.http import HttpResponse
from django.template import loader

def accounts(request):
  template = loader.get_template('mylogin.html')
  return HttpResponse(template.render())
def notice(request):
  return HttpResponse(loader.get_template("mylogin.html").render())