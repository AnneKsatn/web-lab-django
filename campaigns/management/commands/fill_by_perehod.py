from django.core.management.base import BaseCommand
from django.utils import timezone
import requests

from bs4 import BeautifulSoup as BS
import re
from ...models import Campaign

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        page = requests.get('https://club-perexod.ru/')
        bs_page = BS(page.content)

        titles = bs_page.findAll('div', {'class': 'b-schedule-table__name'})
        links = bs_page.findAll('div', {'class': 'b-schedule-table__name'})
        dates = bs_page.findAll('div', {'class': 'b-schedule-table__date'})
        prices = bs_page.findAll('div', {'class': 'b-schedule-table__price-young'})

        for idx in range(len(titles)):
            links[idx] = "https://club-perexod.ru/" + titles[idx].findAll('a')[0].attrs["href"]
            titles[idx] = titles[idx].get_text()
            dates[idx] = dates[idx].get_text()
            prices[idx] = prices[idx].get_text()

        
        for idx in range(len(titles)):
            Campaign.objects.create(title = titles[idx], 
            date=dates[idx], 
            price=prices[idx],
            link=links[idx],
            organizer="Переход: клуб активного отдыха")
