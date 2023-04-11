import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE','udemy_learnings.settings')


import random
import django
django.setup()

from graphs_app.models import Topic,AccessRecord,Webpage

from faker import Faker

fakegen=Faker()
topics =['Search','Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def poplate(N=5):
    for entry in range(N):
        top=add_topic()
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name = fakegen.company()

        webpg=Webpage.objects.get_or_create(Topic=top,url=fake_url,
                                            name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)

if __name__=='__main__':
    print('Populating')
    poplate(100)
    print('complete')