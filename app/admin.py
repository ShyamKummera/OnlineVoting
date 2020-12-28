from django.contrib import admin
from django.contrib.auth.models import User, Group
from app.models import Nominations,ContestantVote

@admin.register(Nominations)
class NomineeAdmin(admin.ModelAdmin):
    list_display = ['no','party_name','party_image']

@admin.register(ContestantVote)
class ContestantVote(admin.ModelAdmin):
    list_display = ['voter_id','voter_name','selected_party','selected_symbol']

admin.site.unregister(User)
admin.site.unregister(Group)
