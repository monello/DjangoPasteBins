# Sometimes you have parent-child (one-to-many) ralationships between your tables.
# In the Admin app you can add all the models one-by-one, by registering them each in the related admin.py 
#    file of the app... but registering each seperately is not very handy whn you have a parent-child 
#    relationship between two tables
# You'd have to enter records to each one separately.
# The ideal way would be to access the parent form, add records to it as normal, but have the option to add child records
#   directly to the parent records
# Django makes this easy throught the use of what they call "Inlines"
# edit your <mysite>/<myapp>/admin.py file

# Create an inline object for the "child" table, we'll use the django tutorial as reference
#    "Choices" is the child table of the "Poll" table i.e. a Poll can have many Choices
@h@class ChoiceInline(admin.StackedInline):
@h@    model = Choice
@h@    extra = 3

# Now we add the "Inline" object to the parent table/object
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date', 'end_date', 'active_date'], 'classes': ['collapse']}),
    ]
@h@    inlines = [ChoiceInline]
    
admin.site.register(Poll, PollAdmin)

### A few notes
# The child is linked to it's parent not the other way around, see: "model = Choice"
# The "extra = 3" option indicates how many open rows you want to display each time the user views the child records
# These "open" rows are used to add new records to the child table.
#
# Note the use of "StackedInline" above? This will, as the name suggests, stack all the child-fields above each other 
#   for each child record.
# This may become messy if your child table has many fields, so another Inline-option exists which will display all the 
#   fields next to each other (in a table-column format) for each child record
# This option is called "TabularInline", simply replace the "StackedInline" in the above eaxmple with this.
# you should now have:

@h@class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# now we add the "Inline" object to the parent table/object
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date', 'end_date', 'active_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    
admin.site.register(Poll, PollAdmin)
