# coding=utf-8
import random
from GameRole import Poker
from GameRole import Player


def shuffle():
    """
    洗牌, 初始化一副扑克牌
    :return:
    """
    poker_list = list()
    base_poker = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    for color in ["黑桃", "方片", "梅花", "红桃"]:
        for value in base_poker:
            poker_list.append(Poker.Poker(color, value))
    big_king = Poker.Poker("红", "joker")
    small_king = Poker.Poker("黑", "joker")
    poker_list.append(big_king)
    poker_list.append(small_king)
    return poker_list


def deal_poker(pokers):
    a_poker, b_poker, c_poker = list(), list(), list()
    flag_a, flag_b, flag_c = True, False, False
    flag = random.choice(pokers)        # 选出先叫分的地主
    while len(pokers) > 0:
        poker = random.choice(pokers)        # 随机取扑克牌
        while True:
            if flag_a:
                a_poker.append(poker)     # 发给A玩家
                flag_a = False                   # 下一次不发给A玩家
                flag_b = True                    # 下一次发给B玩家
                break
            if flag_b:
                b_poker.append(poker)
                flag_b = False
                flag_c = True
                break
            if flag_c:
                c_poker.append(poker)
                flag_c = False
                flag_a = True
                break
        pokers.remove(poker)
    return a_poker, b_poker, c_poker, flag


if __name__ == '__main__':
    pokers_list = shuffle()          # 初始化一副扑克牌
    a_player_poker, b_player_poker, c_player_poker, flag_poke = deal_poker(pokers_list)          # 发牌
    a_player = Player.Player("farmer", a_player_poker)
    b_player = Player.Player("farmer", b_player_poker)
    c_player = Player.Player("farmer", c_player_poker)

    if flag_poke in a_player_poker:
        a_player.identity = "landlord"
    if flag_poke in b_player_poker:
        b_player.identity = "landlord"
    if flag_poke in c_player_poker:
        c_player.identity = "landlord"
    print(str(a_player))
    print(str(b_player))
    print(str(c_player))
