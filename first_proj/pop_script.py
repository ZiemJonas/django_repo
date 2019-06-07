import os
import random
import django
from app.models import AccessRecord, Topic, Webpage
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

django.setup()

# Fake pop script
fake_gen = Faker()
topic = ['search', 'Social', 'Marketplace', 'news', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(random.choice(topic))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):

        # get the topic for the entry
        top = add_topic()

        # create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the new page entry
        wbpg = Webpage.objects.get_or_create(
            topic=top, url=fake_url, name=fake_name)[0]

        # create fake accemss record for the webpage
        acc_rec = AccessRecord.objects.get_or_create(
            name=wbpg, date=fake_date)[0]


if __name__ == '__main__':
    print('populating script!')
    populate(5)
    print('populating complete!')
