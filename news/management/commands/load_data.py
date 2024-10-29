import csv
from django.core.management.base import BaseCommand
from news.models import Article

class Command(BaseCommand):
    help = 'Load data from preprocessed_bbc_news_data.csv into the database'

    def handle(self, *args, **kwargs):
        with open('news/preprocessed_bbc_news_data.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Article.objects.create(
                    category=row['category'].capitalize(),
                    title=row['title'],
                    content=row['content']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded data'))
