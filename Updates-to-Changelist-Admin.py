# there are quite a few nice and easy changes you can apply to Admin with only a few lines of code:
# - making column headers sortable
# - adding filters based on field data type
# - adding searcg functionality
# - adding a date hierarchy filter

# here is the complete code from the Django tutorial

from polls.models import Poll, Choice
from django.contrib import admin
 
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
@h@    list_filter = ['pub_date']
@h@    search_fields = ['question']
@h@    date_hierarchy = 'pub_date'
    
admin.site.register(Poll, PollAdmin)

# modifications to the data model class
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') # note the use of a human readable name, doubles as documentation
    
    def __unicode__(self):
        return self.question
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
@h@    was_published_recently.admin_order_field = 'pub_date'
@h@    was_published_recently.boolean = True
@h@    was_published_recently.short_description = 'Published recently?'
    
### Some notes
# list_filter = ['pub_date'] adds a handy filter to the right of the change-list page
#   these filters are dependent on the field's data type. pub_date is a date time field and thus filters like 
#   - "any date"
#   - "Today"
#   - "Past 7 days" etc, become available
#
# search_fields = ['question'] adds a handy search field to the page
#    you can add as many search fields as you like, but it is suggested to use it within reason
#
# date_hierarchy = 'pub_date' - adds a handy date-drilldown feature. 
#
# "was_published_recently.admin_order_field = 'pub_date'", "was_published_recently.boolean = True" and 
#    "was_published_recently.short_description = 'Published recently?'" are all settings used to make the "was_published_recently"
#    field sortable on the changle list

