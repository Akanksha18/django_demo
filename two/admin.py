from two.models import Position
from django.contrib import admin
from two.models import Choice

#admin.site.register(Poll)

class ChoiceInline(admin.ModelAdmin):
    #model = Choice
    #extra = 2
    fields = ['id', 'pub_date']
    list_display = ('id', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['position']
   
    
class PositionAdmin(admin.ModelAdmin):
   fields = ['name', 'pub_date','position']
   list_display = ('name', 'pub_date', 'position')
   
   list_filter = ['pub_date']
   search_fields = ['position']
   date_hierarchy = 'pub_date'

   
   
   #inlines = [ChoiceInline]
   
admin.site.register(Choice)
admin.site.register(Position, PositionAdmin)


#class PollAdmin(admin.ModelAdmin):
#    fieldsets = [
#        ('Personal information', {'fields': ['name']}),
# 	(None,               {'fields': ['question']}),
#        ('Date information', {'fields': ['pub_date']}),
#   ]

    
#admin.site.register(Poll, PollAdmin)


