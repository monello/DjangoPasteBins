# You control the fields displayed in the change-list, from the form-object in the app's admin.py file 
# Lets reference the Django Tutorial:
# To determine which fields from your model will be used to display in the changelist you specify these 
#   in the "list_display" parameter

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
    ...
@h@    list_display = ('question', 'pub_date', 'was_published_recently')
    
# Note that the "descriptive" names of your fields as used in your model will be displayed.
# For example pub_date above was given a descriptive name of "Date Published", so Django will use that in the 
#    Admin display.
# The question field was not given a descriptive name, just the field name of "question", however Django will make 
#    this prettier by displaying it as "Question" <- note uppercase "Q"
# The last thing to notice here it that 'was_published_recently' is not a field in the model, but a function
# Djando Admin will display the result of this function as the value for each record.
# While we discussing the 'was_published_recently' function, note that Django will prettify this name to, it will become
#    "Was published recently". Django replaces the underscores with spaces and capitalizes the first word.
