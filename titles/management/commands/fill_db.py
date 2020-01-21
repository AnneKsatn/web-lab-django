from django.core.management.base import BaseCommand
from django.utils import timezone
import requests

from bs4 import BeautifulSoup as BS
import re

from ...models import Course

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        page = requests.get('https://openedu.ru')
        bs_page = BS(page.content)

        bs = bs_page.findAll('div', {'class': 'course-title'})

        titles_links = []
        for item in bs:
            titles_links.append(str(item))

        titles_links = " ".join(titles_links)
        course_titles = re.findall(r'(?<=>)[\w\s\.:,\(\)-]*(?=</a>)', titles_links)
        print(course_titles)
        print(len(course_titles))
        
        for item in course_titles:
            Course.objects.create(title = item)
