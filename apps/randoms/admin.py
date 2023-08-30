from django.contrib import admin

from randoms.models.banner import Banner
from randoms.models.bet import Bet


# Register your models here.

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'name',
        'is_active',
        'banner_file'
    )
    list_filter: list[str] = (
        'name',
    )   

@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'game',
        'amount',
        'who',
        'coef',
    )
    list_filter: list[str] = (
        'game',
    ) 
