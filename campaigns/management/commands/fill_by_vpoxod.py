from django.core.management.base import BaseCommand
from django.utils import timezone
import requests

from bs4 import BeautifulSoup as BS
import re
from ...models import Campaign

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        page = requests.get('https://www.vpoxod.ru/allroutes')
        bs_page = BS(page.content)

        dates = bs_page.findAll('div', {'class': 'table_term'})
        names = bs_page.findAll('a', {'class': 'scroll-on-hover ellipsis'})
        prices = bs_page.findAll('span', {'class': 'price-font'})
        links = bs_page.findAll('a', {'class': 'scroll-on-hover ellipsis'})

        for idx in range(len(dates)):
            dates[idx] = dates[idx].get_text()
            names[idx] = names[idx].get_text()
            prices[idx] = prices[idx].get_text().replace(u'\xa0', u' ')
            links[idx] = "https://www.vpoxod.ru/" + links[idx].attrs["href"]

        
        for idx in range(len(dates)):
            Campaign.objects.create(title = names[idx], 
            date=dates[idx], 
            price=prices[idx],
            link=links[idx],
            organizer="vpoXod.ru")
