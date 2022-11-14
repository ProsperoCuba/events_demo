# Event Demo

## Author
GitHub: [https://prosperocuba.github.io/curriculum/](https://prosperocuba.github.io/curriculum/)

Linkedin: [https://linkedin.com/in/armando-gomez-rodriguez-a06baa121](https://linkedin.com/in/armando-gomez-rodriguez-a06baa121)

## Dependencies
- Python v3.8.12
- PostgreSQL v12
- Redis

## Run project
1. Create and activate virtualenv
2. Rename `env.template` to `.env` and fill the values
3. Install requirements: `pip install -r requirements/dev.txt`
4. Apply migration: `python manage.py migrate`
5. Run server `python manage.py runserver`

## Run Test
1. `python manage.py test`