import pytest

import factory
from sghymnal.players.forms import PlayerForm
from sghymnal.players.tests.factories import PlayerFactory, create_image

pytestmark = pytest.mark.django_db


class TestPlayerForm:
    def test_form_valid(self):

        proto_player = PlayerFactory.build()

        data = {
            "name": proto_player.name,
            "country": proto_player.country,
            "position": proto_player.position,
            "squad_number": proto_player.squad_number,
            "team": proto_player.team,
            "twitter": proto_player.twitter,
            "instagram": proto_player.instagram,
        }
        files = {}
        form = PlayerForm(data=data, files=files)

        assert form.is_valid()


# class TestPlayerForm:
#     def test_clean_name(self):
#         proto_player = PlayerFactory.build()

#         form = PlayerFactory(
#             {
#                 "name": proto_player.name,
#                 "country": proto_player.country,
#                 "position": proto_player.position,
#                 "squad_number": proto_player.squad_number,
#                 "team": proto_player.team,
#                 "instagram": proto_player.instagram,
#                 "twitter": proto_player.twitter,
#                 "thumbnail": proto_player.thumbnail,
#             }
#         )

#         assert form.is_valid()
