from django.core.management.base import BaseCommand

import csv

from searchlocations.models import Location

class Command(BaseCommand):
    def handle(self, **options):
        fhand = open('searchlocations/load.csv')
        reader = csv.reader(fhand)
        next(reader)  # Advance past the header
        Location.objects.all().delete()
        for row in reader:
            m = Location(
                city=row[0],
                region=row[5],
                area='0.0',
                products='null',
            )
            print(m.region)
            m.save()