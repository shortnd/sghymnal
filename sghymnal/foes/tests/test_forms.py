import pytest

from sghymnal.foes.forms import FoeForm
from sghymnal.foes.tests.factories import FoeFactory

pytestmark = pytest.mark.django_db


# class TestFoeForm:
#     def test_form_valid(self):
#         proto_foe = FoeFactory.build()

#         data = {
#             "opponent": proto_foe.opponent,
#             "competition": proto_foe.competition,
#             "logo": proto_foe.logo,
#             "background_color": proto_foe.background_color,
#             "accent_color": proto_foe.accent_color,
#             "text_color": proto_foe.text_color,
#             "season": proto_foe.season,
#             "active": proto_foe.active,
#         }

#         form = FoeForm(data)

#         assert form.is_valid()
