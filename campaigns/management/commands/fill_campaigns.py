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

        bs_names = bs_page.findAll('a', {'class': 'scroll-on-hover ellipsis'})
        bs_date = bs_page.findAll('div', {'class': 'table_term'})
        bs_price = bs_page.findAll('span', {'class': 'price-font'})
        bs_links = bs_page.findAll('a', {'class': 'scroll-on-hover ellipsis'})

        for idx, date in enumerate(bs_date):
            bs_date[idx] = date.findAll('div')
            bs_date[idx] = bs_date[idx][0].get_text()

            bs_names[idx] = bs_names[idx].get_text()
            bs_price[idx] = bs_price[idx].get_text().replace(u'\xa0', u' ')
            bs_links[idx] = "https://www.vpoxod.ru/" + bs_links[idx].attrs["href"]

        
        for idx, item in enumerate(bs_names):
            Campaign.objects.create(title = bs_names[idx], 
            date=bs_date[idx], 
            price=bs_price[idx],
            link=bs_links[idx])
