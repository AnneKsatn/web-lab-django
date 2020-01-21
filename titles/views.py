from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Course

# Create your views here.
def title_home(request):

    queryset = Course.objects.all()
    context = {'queryset': queryset, 'title': 'Course list'}

    return render(request, 'index.html', context)