
import json
import sys

class Player:
    VERSION = "1.6"

    def betRequest(self, game_state):
        current_buyin = (game_state["current_buy_in"])
        small_blind = game_state["small_blind"]
        in_action = game_state["in_action"]
        player_list = game_state
        hole_cards = []
        comm_cards = game_state["community_cards"]
        minimum_raise = game_state["minimum_raise"]
        for player in game_state["players"]:
            if player["name"] == "CantoBright":
                hole_cards = player["hole_cards"]





        # if current_buyin > small_blind * 4:
        #     return 0
        if hole_cards[0]["rank"] == hole_cards[1]["rank"] or hole_cards[0]["rank"] in ["J", "Q", "K", "A"] or hole_cards[1]["rank"] in ["J", "Q", "K", "A"]:
            if comm_cards and (hole_cards[0]["rank"] == hole_cards[1]["rank"]\
                    or hole_cards[0]["rank"] in [comm_cards[i]["rank"] for i in range(3)]\
                    or hole_cards[1]["rank"] in [comm_cards[i]["rank"] for i in range(3)]):
                return current_buyin - game_state["players"][in_action]["bet"] + minimum_raise * 2
            return current_buyin - game_state["players"][in_action]["bet"] + minimum_raise
        else:
            print(hole_cards, sys.stderr)

            return current_buyin - game_state["players"][in_action]["bet"]

    def showdown(self, game_state):
        pass

