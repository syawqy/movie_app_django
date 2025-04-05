# Movie App

A simple web-based movie application built with Django. This app allows users to browse a list of movies, view detailed information about each movie, and search for movies by name.

## Features

- Movie Listing Page: Displays a list of movies with images, names, and ratings.
- Movie Detail Page: Provides detailed information about each movie, including a description, MPAA rating, duration, language, and genres.
- Search Functionality: Users can search for movies by name, with results filtered in real-time.

## Technologies Used

- Python
- Django
- SQLite (as the database)
- HTML/CSS/JavaScript

## Installation

### Prerequisites

- Python 3.x
- Django

### Steps to Set Up

1. Clone the repository:
   ```bash
   git clone https://github.com/syawqy/movie_app_jango.git
   cd movie_app
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

5. Seed the database with movie data:
   ```bash
   python manage.py seed_movies path/to/your/movies.json
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your web browser and go to `http://127.0.0.1:8000/` to view the app.

## Usage

- Use the search bar on the movie listing page to find movies by name.
- Click on a movie title to view its details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to the Django community for their amazing framework.
- Inspired by various movie database applications.
