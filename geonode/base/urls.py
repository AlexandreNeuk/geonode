
#########################################################################
#
# Copyright (C) 2019 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################


from django.conf.urls import url

from .views import (
    ResourceBaseAutocomplete, RegionAutocomplete,
    HierarchicalKeywordAutocomplete, ThesaurusKeywordLabelAutocomplete, OwnerRightsRequestView,
	EmbrapaKeywordsAutocomplete, EmbrapaUnityAutocomplete, EmbrapaPurposeAutocomplete, EmbrapaDataQualityStatementAutocomplete,
    EmbrapaAuthorsAutocomplete)


urlpatterns = [
    url(
        r'^autocomplete_response/$',
        ResourceBaseAutocomplete.as_view(),
        name='autocomplete_base',
    ),

    url(
        r'^autocomplete_region/$',
        RegionAutocomplete.as_view(),
        name='autocomplete_region',
    ),

    url(
        r'^autocomplete_hierachical_keyword/$',
        HierarchicalKeywordAutocomplete.as_view(),
        name='autocomplete_hierachical_keyword',
    ),
    url(
        r'^thesaurus_autocomplete/$',
        ThesaurusKeywordLabelAutocomplete.as_view(),
        name='thesaurus_autocomplete',
    ),
    url(
        r'^autocomplete_embrapa_keywords/$',
        EmbrapaKeywordsAutocomplete.as_view(),
        name='autocomplete_embrapa_keywords',
    ),
    url(
        r'^autocomplete_embrapa_unity/$',
        EmbrapaUnityAutocomplete.as_view(),
        name='autocomplete_embrapa_unity',
    ),
    url(
        r'^autocomplete_embrapa_purpose/$',
        EmbrapaPurposeAutocomplete.as_view(),
        name='autocomplete_embrapa_purpose',
    ),
    url(
        r'^autocomplete_embrapa_data_quality_statement/$',
        EmbrapaDataQualityStatementAutocomplete.as_view(),
        name='autocomplete_embrapa_data_quality_statement',
    ),
    url(
        r'^autocomplete_embrapa_autores/$',
        EmbrapaAuthorsAutocomplete.as_view(),
        name='autocomplete_embrapa_autores',
    ),
    url(
        r'^resource_rights/(?P<pk>\d+)$',
        OwnerRightsRequestView.as_view(),
        name='owner_rights_request',
    ) 
]
