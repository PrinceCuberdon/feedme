# -*- coding: UTF-8 -*-
# 
# FeedMe (c) Prince Cuberdon 2011 and Later <princecuberdon@bandcochon.fr>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from django.contrib import admin

from feedme.models import FeedMe, SearchEngine

class FeedMeAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','creation', 'url', )
    date_hierarchy = 'creation'
    
class SearchEngineAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'url', 'ping_count', 'active', )
    list_editable = ('active', )

admin.site.register(FeedMe, FeedMeAdmin)
admin.site.register(SearchEngine, SearchEngineAdmin)
