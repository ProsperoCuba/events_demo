# Event Demo

## Author
GitHub: [https://prosperocuba.github.io/curriculum/](https://prosperocuba.github.io/curriculum/)

Linkedin: [https://linkedin.com/in/armando-gomez-rodriguez-a06baa121](https://linkedin.com/in/armando-gomez-rodriguez-a06baa121)

## Dependencies
- Python v3.8.12
- PostgreSQL v12
- Redis

## Run project
2. Create and activate virtualenv
3. Rename `env.template` to `.env` and fill the values
4. Install requirements: `pip install -r requirements/dev.txt`
5. Apply migration: `python manage.py migrate`
6. Create user as superuser
7. Run server `python manage.py runserver`
8. API docs url: `/api/v1/docs`
9. django-admin url: `/support`

## Run Test
1. `python manage.py test`
2. Folder implementation rooms/test.py