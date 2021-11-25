![alt text](https://raw.githubusercontent.com/renz-b/Tester/master/app/static/favicon.ico "Logo") **Tester**

_A small web app that serves multiple choice questions_

![alt text](https://raw.githubusercontent.com/renz-b/Tester/master/app/static/favicon.ico "Logo") [Quick Tester](https://quick-tester.herokuapp.com/ "Quick Tester")

Website is made with Flask as backend with Jinja2 and Flask-Bootsrap to render frontend with some custom CSS added. JQuery and AJAX for form submissions to refresh multiple choice questions without reloading the page. Database used started with SQLite3 then migrated to PostgreSQL for easier hosting to Heroku.

Other extensions used were: FlaskSQLAlchemy (database operations), Flask-Nav (navbar rendering), Flask-WTForms (form rendering and backend logic), Fkask-SSLify (security).

## Features
- Integrated a log in and register form while those who do not want to register have the guest user link that shows 5 random questions. Registered users can chose subject and number of questinos per page.
- Did my best for website to be mobile friendly
- Admin privilidges only include able to add questions, feature only shows if admin user is logged in and hidden from regular users
- Answering questions does not refresh page due to AJAX and JQuery
- Uses PostgreSQL database hosted in heroku
