from django.contrib import admin
from .models import User,Sales,Store,Trash,Reciepts
# Register your models here.
admin.site.register(User)
admin.site.register(Sales)
admin.site.register(Store)
admin.site.register(Trash)
admin.site.register(Reciepts)
