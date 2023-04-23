import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord,WebPage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populating(N=5):
    for i in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = WebPage.objects.get_or_create(topic=top,name=fake_name,url = fake_url)[0]
        accr = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

if __name__ == '__main__':
    print('populating records')
    populating(15)
    print('populating complete!')
