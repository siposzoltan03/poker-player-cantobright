
import json
import sys

class Player:
    VERSION = "1.2"

    def betRequest(self, game_state):
        current_buyin = (game_state["current_buy_in"])
        small_blind = game_state["small_blind"]
        in_action = game_state["in_action"]
        player_list = game_state
        hole_cards = []
        minimum_raise = game_state["minimum_raise"]
        for player in game_state["players"]:
            if player["name"] == "CantoBright":
                hole_cards = player["hole_cards"]

        if current_buyin > small_blind * 4:
            return 0
        elif hole_cards[0]["rank"] == hole_cards[1]["rank"] or hole_cards[0]["rank"] in ["J", "Q", "K", "A"] or hole_cards[1]["rank"] in ["J", "Q", "K", "A"]:
            return current_buyin - game_state["players"][in_action]["bet"] + minimum_raise
        else:
            # print(hole_cards, sys.stderr)

            return current_buyin - game_state["players"][in_action]["bet"]

    def showdown(self, game_state):
        pass

