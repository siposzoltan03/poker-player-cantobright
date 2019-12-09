import json
import sys


class Player:
    VERSION = "3.2"

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

        if len(comm_cards) == 0:
            # return game_state["players"][in_action]["stack"]

            # if current_buyin > 500:
            #     return 0
            # if hole_cards[0]["rank"] == hole_cards[1]["rank"] or (hole_cards[0]["rank"] in ["J", "Q", "K", "A"] and
            #         hole_cards[1]["rank"] in ["J", "Q", "K", "A"]):
            #     return current_buyin - game_state["players"][in_action]["bet"] + game_state["players"][in_action][
            #         "stack"] / 4
            if hole_cards[0]["rank"] == hole_cards[1]["rank"] or (hole_cards[0]["rank"] in ["J", "Q", "K", "A"] and
                    hole_cards[1]["rank"] in ["J", "Q", "K", "A"]):
                return current_buyin - game_state["players"][in_action]["bet"] + minimum_raise
            if hole_cards[0]["rank"] == hole_cards[1]["rank"] or (hole_cards[0]["rank"] in ["J", "Q", "K", "A"] or
                    hole_cards[1]["rank"] in ["J", "Q", "K", "A"]):
                return current_buyin - game_state["players"][in_action]["bet"]
            return 0
        elif len(comm_cards) == 3:
            all_cards = [comm_cards[0]["suit"], comm_cards[1]["suit"], comm_cards[2]["suit"], hole_cards[0]["suit"],
                         hole_cards[1]["suit"]]
            rank_cards = [comm_cards[0]["rank"], comm_cards[1]["rank"], comm_cards[2]["rank"], hole_cards[0]["rank"],
                          hole_cards[1]["rank"]]
            if (hole_cards[0]["rank"] == hole_cards[1]["rank"]
                    or hole_cards[0]["rank"] in [comm_cards[i]["rank"] for i in range(3)]
                    or hole_cards[1]["rank"] in [comm_cards[i]["rank"] for i in range(3)]):
                return current_buyin - game_state["players"][in_action]["bet"] + minimum_raise

            if len(set(all_cards)) < 3 or len(set(rank_cards)) <= 3:
                return game_state["players"][in_action]["stack"]
            return current_buyin - game_state["players"][in_action]["bet"]
        elif len(comm_cards) == 4:
            all_cards = [comm_cards[0]["suit"], comm_cards[1]["suit"], comm_cards[2]["suit"], comm_cards[3]["suit"],
                         hole_cards[0]["suit"],
                         hole_cards[1]["suit"]]
            rank_cards = [comm_cards[0]["rank"], comm_cards[1]["rank"], comm_cards[2]["rank"], comm_cards[3]["rank"],
                          hole_cards[0]["rank"],
                          hole_cards[1]["rank"]]
            if (hole_cards[0]["rank"] == hole_cards[1]["rank"]
                    or hole_cards[0]["rank"] in [comm_cards[i]["rank"] for i in range(3)]
                    or hole_cards[1]["rank"] in [comm_cards[i]["rank"] for i in range(3)]):
                return current_buyin - game_state["players"][in_action]["bet"] + minimum_raise

            if len(set(all_cards)) < 3 or len(set(rank_cards)) <= 3:
                return game_state["players"][in_action]["stack"]
            return current_buyin - game_state["players"][in_action]["bet"]
        elif len(comm_cards) == 5:
            all_cards = [comm_cards[0]["suit"], comm_cards[1]["suit"], comm_cards[2]["suit"], comm_cards[3]["suit"],
                         comm_cards[4]["suit"],
                         hole_cards[0]["suit"],
                         hole_cards[1]["suit"]]
            rank_cards = [comm_cards[0]["rank"], comm_cards[1]["rank"], comm_cards[2]["rank"], comm_cards[3]["rank"],
                          comm_cards[4]["rank"],
                          hole_cards[0]["rank"],
                          hole_cards[1]["rank"]]
            if (hole_cards[0]["rank"] == hole_cards[1]["rank"]
                    or hole_cards[0]["rank"] in [comm_cards[i]["rank"] for i in range(3)]
                    or hole_cards[1]["rank"] in [comm_cards[i]["rank"] for i in range(3)]):
                return current_buyin - game_state["players"][in_action]["bet"] + minimum_raise

            if len(set(all_cards)) < 3 or len(set(rank_cards)) <= 3:
                return game_state["players"][in_action]["stack"]
            return current_buyin - game_state["players"][in_action]["bet"]
        else:
            print(hole_cards, sys.stderr)

            return 0

    def showdown(self, game_state):
        pass
