from django.shortcuts import render
from .models import Campaign
from django.shortcuts import render_to_response
from django.http import HttpResponse

def campaign_home(request):
    queryset = Campaign.objects.all()
    context = {'queryset': queryset, 'title': ' Доступные походы'}
    return render(request, 'camp.html', context)
