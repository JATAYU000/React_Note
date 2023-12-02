from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
	list_display = ('id','title','description','dueDate')
# Register your models here.

admin.site.register(Note, NoteAdmin)