# coding=utf-8


class Player(object):

    def __init__(self, identity, pokers):
        """
        定义玩家身份和手中的扑克牌
        :param identity:
        :param pokers:
        """
        self.identity = identity
        self.pokers = pokers

    def __str__(self):
        info = list()
        for poker in self.pokers:
            info.append(str(poker))
        return self.identity + ", " + ",".join(info)
