# here's how to re-order the fields displayed in the form of one of your apps in the admin side
# edit the admin.py file inside our app: <mysite>/<appname>/admin.py
# add an Admin function as follows
# 1. Assuming the app name is "Poll" as in the Django tutorial, you will create a new class and call it PollAdmin 
#       You can name it anything, but this is a since convention used in Django
# 2. List the order of the fields inside this class
#       You should now have the following:

class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']
    
# register the PollAdmin class, so the admis app know about it
admin.site.register(Poll, PollAdmin)
