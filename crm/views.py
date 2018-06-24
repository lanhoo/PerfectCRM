from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    # request.GET.setdefault('next', default='/crm/')
    return render(request, 'index.html')
