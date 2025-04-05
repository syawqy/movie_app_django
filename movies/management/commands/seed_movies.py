import json
from django.core.management.base import BaseCommand
from movies.models import Movie, MpaaRating

class Command(BaseCommand):
    help = 'Populate database with movie data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file']) as f:
            movies_data = json.load(f)
        
        # First create all MPA ratings
        mpaa_ratings = {}
        for data in movies_data:
            mpaa_data = data['mpaaRating']
            if mpaa_data['type'] not in mpaa_ratings:
                rating, _ = MpaaRating.objects.get_or_create(
                    type=mpaa_data['type'],
                    defaults={'label': mpaa_data['label']}
                )
                mpaa_ratings[mpaa_data['type']] = rating
        
        # Then create movies
        for data in movies_data:
            Movie.objects.update_or_create(
                id=data['id'],
                defaults={
                    'name': data['name'],
                    'description': data['description'],
                    'img_path': data['imgPath'],
                    'duration': data['duration'],
                    'genre': data['genre'],
                    'language': data['language'],
                    'mpaa_rating': mpaa_ratings[data['mpaaRating']['type']],
                    'user_rating': data['userRating']
                }
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))