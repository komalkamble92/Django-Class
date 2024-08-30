'''

# Install Django
pip install django 

# Start a new project
django-admin startproject project_name 

# Start a new project in the current directory
django-admin startproject project_name2 .

# Run the development server
python manage.py runserver

# Response:
# System check identified no issues (0 silenced).
# August 25, 2024 - 14:56:44
# Django version 5.1, using settings 'project_name.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CONTROL-C.

# Apply migrations
python manage.py migrate

# Response:
# You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
# Run 'python manage.py migrate' to apply them.

# Applying migrations:
# Applying contenttypes.0001_initial... OK
# Applying auth.0001_initial... OK
# Applying admin.0001_initial... OK
# Applying admin.0002_logentry_remove_auto_add... OK
# Applying admin.0003_logentry_add_action_flag_choices... OK
# Applying contenttypes.0002_remove_content_type_name... OK
# Applying auth.0002_alter_permission_name_max_length... OK
# Applying auth.0003_alter_user_email_max_length... OK
# Applying auth.0004_alter_user_username_opts... OK
# Applying auth.0005_alter_user_last_login_null... OK
# Applying auth.0006_require_contenttypes_0002... OK
# Applying auth.0007_alter_validators_add_error_messages... OK
# Applying auth.0008_alter_user_username_max_length... OK
# Applying auth.0009_alter_user_last_name_max_length... OK
# Applying auth.0010_alter_group_name_max_length... OK
# Applying auth.0011_update_proxy_permissions... OK
# Applying auth.0012_alter_user_first_name_max_length... OK
# Applying sessions.0001_initial... OK

# Admin login URL
http://127.0.0.1:8000/admin/login/?next=/admin/

# Create a superuser
python manage.py createsuperuser

# Response:
# (venv_name) ➜  project_name git:(main) ✗ python manage.py createsuperuser
# Username (leave blank to use 'akansha'): admin
# Email address: admin@admin.com
# Password: 
# Password (again): 
# The password is too similar to the username.
# This password is too short. It must contain at least 8 characters.
# This password is too common.
# Bypass password validation and create user anyway? [y/N]: y
# Superuser created successfully.

'''