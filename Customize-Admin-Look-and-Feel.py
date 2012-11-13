# Admin also works from the Django template system
# To change the look and feel of a the Admin side you need to overide a template

# First you need to ensure that Django knows where you save all you templates
# You can provide many locations, the best if probably to provide 1 main locations and split it
#   into various app specific locations using folders under that.

# edit the project's settings.py file (<mysite>/settings.py)
# add your template directory to the TEMPLATE_DIRS list
# Mine looks like this

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    'D:/work/django/testapp/templates',
) 

# now go copy the admin/base_site.html template from the main django instance (inside your python site-packages folder)
# I use a virtual environment so mine is at: C:/vpe/testapp/Lib/site-packages/django/contrib/admin/templates/admin/
# copy the base_site.html template to you specified templates folder as per TEMPLATE_DIRS above
# create an "admin" folder inside your templates folder and paste the template there.
#
# You can now edit this file and Django will use this one instead of the django main instance one
#
# Django does all these checks for you, you don't need to do anything else.
# 
# Example: You can now edit the "Django administration" text to what you want.
# If you know Django's templating language there are plenty of things you can do here
#  