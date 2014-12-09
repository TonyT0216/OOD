__author__ = 'Tony'

import rpyc
import ProxyPlayer
class RPYCProxyPlayer(ProxyPlayer.ProxyPlayer):

    def __init__(self):
        ProxyPlayer.ProxyPlayer.__init__(self)

    def exposed_play(self):
        return self.ProxyPlayer