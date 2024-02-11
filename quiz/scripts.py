# create_quiz_categories.py

import json
from quiz.models import QuizCategory, Quiz

def create_quiz_categories():
    categories_data = [
            {
                'name': 'History',
                'description': 'Journey through the events and stories that shaped the world.',
                'keywords': ['Ancient History', 'Medieval History', 'Modern History', 'World Wars'],
            },
            {
                'name': 'Geography',
                'description': 'Discover the diverse landscapes, cultures, and physical features of the Earth.',
                'keywords': ['Countries', 'Capitals', 'Landforms', 'Cultures', 'Geopolitics'],
            },
            {
                'name': 'Technology',
                'description': 'Explore the latest advancements and innovations in the world of technology.',
                'keywords': ['Programming', 'Cybersecurity', 'Artificial Intelligence', 'Gadgets'],
            },
            {
                'name': 'Literature',
                'description': 'Immerse yourself in the world of literature, from classic to contemporary works.',
                'keywords': ['Novels', 'Poetry', 'Authors', 'Literary Movements'],
            },
            {
                'name': 'Music',
                'description': 'Dive into the melody and rhythm of different musical genres and artists.',
                'keywords': ['Genres', 'Artists', 'Instruments', 'Music History'],
            },
            {
                'name': 'Mathematics',
                'description': 'Challenge your logical and mathematical reasoning skills.',
                'keywords': ['Algebra', 'Geometry', 'Calculus', 'Statistics'],
            },
    ]

    for category_data in categories_data:
        QuizCategory.objects.create(
            name=category_data['name'],
            description=category_data['description'],
            keywords=json.dumps(category_data['keywords']),
        )

if __name__ == "__main__":
    create_quiz_categories()
