# coding=utf-8


class Poker(object):

    def __init__(self, color, value):
        """
        定义扑克牌的花色和面值
        :param color:
        :param value:
        """
        self.color = color
        self.value = value

    def __str__(self):
        return "".join([self.color, self.value])
