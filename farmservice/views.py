from django.template import loader
from django.shortcuts import render


from django.contrib.auth.decorators import login_required



@login_required(login_url='/accounts/login')
def home(request):
    print()
    return render(request, 'service/index.html', {})
