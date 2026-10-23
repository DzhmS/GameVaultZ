# GameVaultZ

GameVaultZ is a Django web application for managing a personal game collection.

Users can create and manage games, genres, platforms, and reviews through the application's user interface.

## Features

- Create, view, edit, and delete games
- Manage genres
- Manage gaming platforms
- Create and manage game reviews
- Filter games by genre and platform
- Sort games by title and release date
- Upload images for games
- Custom rating labels for reviews
- Custom 404 page
- Responsive Bootstrap design
- Navigation between all main sections

## Technologies

- Python 3.11
- Django 5.2
- SQLite
- Bootstrap 5
- Pillow
- HTML
- CSS

## Project Structure

```text
GameVaultZ/
├── gamevaultz/
├── games/
├── platforms/
├── reviews/
├── static/
├── templates/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Open the project directory:

```bash
cd GameVaultZ
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment.

On Windows:

```bash
.venv\Scripts\activate
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

6. Apply the database migrations:

```bash
python manage.py migrate
```

7. Start the development server:

```bash
python manage.py runserver
```

8. Open the application in your browser:

```text
http://127.0.0.1:8000/games/
```

## Main Models

### Game
Stores information about games, including title, description, release date, developer, publisher, genres, platforms, and an optional image.

### Genre
Stores game genres and their descriptions.

### Platform
Stores gaming platforms and their descriptions.

### Review
Stores a review for a game, including a rating from 1 to 100, comment, and creation date.

## Relationships

- Game ↔ Genre — Many-to-Many
- Game ↔ Platform — Many-to-Many
- Review → Game — Many-to-One

## Forms and Validation

The application uses Django ModelForms for creating and editing data.

The forms include:
- Custom labels
- Help texts
- Placeholders
- Validation messages
- A disabled field when editing a review
- Delete confirmation pages

Review ratings are limited to values between 1 and 100.

## Navigation

The navigation bar provides access to:

- Games
- Genres
- Platforms
- Reviews
- Add Game
- Add Genre
- Add Platform
- Add Review

All main application pages are accessible through the user interface.

## Additional Functionality

The project includes:

- Game filtering by genre
- Game filtering by platform
- Sorting by title
- Sorting by release date
- Built-in Django template filters
- A custom `score_label` template filter
- Custom 404 error handling
- Optional game image uploads
- Reusable base template, navbar, and footer

## Notes

The application is designed to work with an empty database.

All required objects can be created through the website interface without using the Django admin panel.

Game images are optional and are stored in the media directory.

No authentication or user management system is required for this project.