from django.contrib import admin

from .models import Animals
from .models import Donaters
from .models import Caretakers

admin.site.register(Animals)
admin.site.register(Donaters)
admin.site.register(Caretakers)