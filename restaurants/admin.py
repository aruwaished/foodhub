from django.contrib import admin
from .models import Restaurant


class RestaurantModeAdmin(admin.ModelAdmin):
	list_display = ["name", "description", "id"]
	list_filter = ["name"]
	search_fields = ["description",]
	list_display_links = ["name",]

	class Meta:
		model = Restaurant

admin.site.register(Restaurant, RestaurantModeAdmin)