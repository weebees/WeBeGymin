#!/bin/bash

# Create core application structure within the current WeBeGymin folder
mkdir -p app/{routes,templates/{auth,sleep,food,workout},static/{css,js}}
touch app/__init__.py app/models.py

# Create route files for each feature
touch app/routes/{__init__.py,auth.py,sleep.py,food.py,workout.py}

# Create static files
touch app/static/css/style.css app/static/js/scripts.js

# Create templates for each section
touch app/templates/{base.html,index.html}
touch app/templates/auth/{login.html,register.html}
touch app/templates/sleep/sleep.html
touch app/templates/food/food.html
touch app/templates/workout/workout.html

# Create configuration and other essential files if not present
touch config.py run.py README.md

# Set up database migrations and testing directories
mkdir -p migrations tests
touch tests/{test_auth.py,test_sleep.py,test_food.py,test_workout.py}

echo "Project scaffold within 'We Be Gymin' has been created!"
