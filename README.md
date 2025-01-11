# Django Polls Playwright Demo

UI Testing the Django Tutorial Polls app with Python Playwright

### Setup

The application is configured to use Postgres.

See config/settings.py and tests/settings.py and create the database and users to match.

In psql
```
CREATE USER demo_app_user WITH PASSWORD 'supersecret';
CREATE DATABASE django_polls_playwright_demo WITH OWNER demo_app_user;
GRANT ALL PRIVILEGES ON DATABASE django_polls_playwright_demo TO demo_app_user;

create user demo_app_tester with password 'verysecret'
alter user demo_app_tester CREATEDB;
```

During the test run, it will create a database with the NAME specified in tests/settings.py, prepended with `test_`.

### Run the tests

To run the tests and see it open the browser and view the page:
```
pytest --headed --slowmo 2000
```

### License
* https://wsmoak.mit-license.org/

### References
* https://docs.djangoproject.com/en/5.1/intro/tutorial01/
