# In the Django Admin section, you can split your form fields up into fieldsets.

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date', 'end_date', 'active_date']}),
    ]
    
admin.site.register(Poll, PollAdmin)

# you will notice that you can name/header each fieldset
# in the example above the field fieldset was not name so "None" was used
# the second fieldset was named "Date Information"
# you list all the fields in the fields-list as demonstrated in the 'Date Information' fieldset above

# here is the same form fieldsets, but set as collasible fieldsets
# you do this by attaching the "collapse" class to a fieldset

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {
                'fields': ['pub_date', 'end_date', 'active_date'], 
@h@                'classes': ['collapse']
                }
        ),
    ]
    
admin.site.register(Poll, PollAdmin)