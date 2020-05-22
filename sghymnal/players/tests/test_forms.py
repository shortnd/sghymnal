import pytest

# from sghymnal.players.forms import PlayerForm
# from sghymnal.players.tests.factories import PlayerFactory

pytestmark = pytest.mark.django_db


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
