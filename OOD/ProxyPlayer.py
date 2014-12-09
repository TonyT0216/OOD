__author__ = 'Pat and Tony'

import rpyc
import Player
import RPSPlayer

"ProxyPlayer class uses Player class with a Proxy Pattern"
class ProxyPlayer(Player.Player):
    """ The Proxy of the RPSPlayer
    """
    def __init__(self, player):
        self._player = Player()

    def play(self):
        return self._player.play()

    def get_name(self):
        return self._player.get_name()
    # def load(self):
    #     print("loading ".format(self._player.get_name))
    #     self._loaded = True

    # def find_player(self,person):
    #     return self._player.find_player()
    #
    #
    # def me_playing_against(self,person):
    #     return self._player.me_playing_against()
    #
    # def match_results(self, person, played):
    #     return self._player.match_results()
    #
    # def notify(self, msg):
    #     return self._player.notify()
    #
    # def play(self, position=None):
    #     return self._player.play()
    #
    #
    # def get_name(self):
    #     return self._player.get_name()

if __name__ == "__main__":
    p1 = ProxyPlayer(RPSPlayer)
    p1.get_name()
    # fake_moves = (1,2)
    # fake_result = (0,1)
    #
    # player.notify(Message.Message.get_match_start_message(players))
    # player.notify(Message.Message.get_round_start_message(players))
    # move = player.play()
    # print ("Move played: ", move)
    # player.notify(Message.Message.get_round_end_message(players,fake_moves,fake_result))