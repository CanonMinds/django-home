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
            print(row)

        m = Location(
            city=row[0],
            region=row[1],
            area=row[2],
            products=row[3]
        )
        m.save()