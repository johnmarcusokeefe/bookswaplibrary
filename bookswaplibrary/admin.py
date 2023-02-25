from django.contrib import admin

# Register your models here.

from .models import Member, Address, Book, BookInstance

admin.site.register(Member)
admin.site.register(Address)
admin.site.register(Book)
admin.site.register(BookInstance)