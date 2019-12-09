
import json
import sys

class Player:
    VERSION = "1.0"

    def betRequest(self, game_state):
        current_buyin = (game_state["current_buy_in"])
        small_blind = game_state["small_blind"]
        in_action = game_state["in_action"]

        if current_buyin > small_blind * 2:
            return 0
        else:
            # print(message, file=sys.stderr)
            return current_buyin - game_state["players"][in_action]["bet"]

    def showdown(self, game_state):
        pass

