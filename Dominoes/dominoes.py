from math import remainder
import random as rnd
from typing import Counter
import time


class CantAddBone(Exception):
    pass


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.hand = []

    def take_bone(self, bone):
        self.hand.append(bone)

    def place_bone(self, bone):
        self.hand.remove(bone)

    def make_move(self, choosen_bone, dominoes):
        choosen_bone = int(choosen_bone)

        if choosen_bone == 0:
            if dominoes.stack:
                rnd_ = rnd.choice(dominoes.stack)
                dominoes.stack.remove(rnd_)
                self.hand.append(rnd_)
        elif choosen_bone > 0:
            dominoes.put_bone(self.hand[abs(choosen_bone)-1], -1, self)
        elif choosen_bone < 0:
            dominoes.put_bone(self.hand[abs(choosen_bone)-1], 0, self)

    def bone_from_stack(self, dominoes):
        if dominoes.stack:
            rnd_ = rnd.choice(dominoes.stack)
            dominoes.stack.remove(rnd_)
            self.hand.append(rnd_)


class PC(Player):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_move(self, dominoes):
        full_stack = []
        full_stack.extend(dominoes.stack)
        full_stack.extend(self.hand)

        assessment = Counter([z for x in full_stack for z in x])

        hand_with_assessment = []

        for set_ in self.hand:
            hand_with_assessment.append(
                [set_, assessment.get(set_[0]) + assessment.get(set_[1])])

        for set_ in sorted(hand_with_assessment, key=lambda x: x[1], reverse=True):
            try:
                dominoes.put_bone(set_[0], 0, self)
                break
            except CantAddBone:
                try:
                    dominoes.put_bone(set_[0], -1, self)
                    break
                except CantAddBone:
                    continue
        else:
            super().bone_from_stack(dominoes)


class Dominoes:
    bones = []
    Player1 = Player('Player1')
    PC = PC('PC')
    players = [Player1, PC]
    stack = []
    table = [None]
    turn = None
    status = True

    def __init__(self) -> None:
        while not self.table[0]:
            self.get_bones()
            self.deal_bones()
            self.shuffle_stack_bones()
            self.get_start_bone()

        while self.show_table() or self.status:
            if self.turn == self.Player1.name:
                player = self.Player1

                while True:
                    try:
                        choosen_bone = input('Choose what to put')
                        player.make_move(choosen_bone, self)
                        break
                    except CantAddBone:
                        print('Cant add this bone')
                    except Exception:
                        print('Choose bone from the list')

                self.turn = self.PC.name
            else:
                time.sleep(2)
                player = self.PC
                player.make_move(self)
                self.turn = self.Player1.name

            self.check_status()

    def check_status(self):
        if len(self.PC.hand) == 0:
            print('PC win!')
            self.status = False
        elif len(self.Player1.hand) == 0:
            print('Player1 win!')
            self.status = False
        elif self.table[0][0] == self.table[-1][1]\
                and Counter([a for b in self.table for a in b]).get(self.table[0][0]) == 8:
            print('ITS DRAW!')
            self.status = False

    def get_bones(self):
        start = 0

        for i in range(0, 7):
            for j in range(start, 7):
                self.bones.append([i, j])

            start += 1

    def deal_bones(self):
        for player in self.players:
            for _ in range(7):
                set_ = rnd.choice(self.bones)
                player.take_bone(set_)
                self.bones.remove(set_)

    def shuffle_stack_bones(self):
        for _ in range(len(self.bones)):
            self.stack.append(rnd.choice(self.bones))
            self.bones.remove(self.stack[-1])

    def get_start_bone(self):
        max_double = None
        whos_max_double = None

        for player in self.players:
            for set_ in player.hand:
                if set_[0] == set_[1]:
                    if not max_double:
                        max_double = set_
                        whos_max_double = player
                    else:
                        if set_[0] > max_double[0]:
                            max_double = set_
                            whos_max_double = player

        if max_double:
            whos_max_double.place_bone(max_double)
            self.turn = whos_max_double.name
            self.table[0] = max_double

    def put_bone(self, bone, side, player):
        if side == -1:
            if bone[0] == self.table[side][1]:
                self.table.append(bone)
            elif bone[1] == self.table[side][1]:
                self.table.append(list(reversed(bone)))
            else:
                raise CantAddBone
        if side == 0:
            if bone[1] == self.table[side][0]:
                self.table.insert(0, bone)
            elif bone[0] == self.table[side][0]:
                self.table.insert(0, list(reversed(bone)))
            else:
                raise CantAddBone

        player.place_bone(bone)

    def show_table(self):
        loc_table = None

        if len(self.table) >= 7:
            loc_table = [
                self.table[0],
                self.table[1],
                self.table[2],
                '...',
                self.table[-3],
                self.table[-2],
                self.table[-1]]
        print()
        print('=' * 70)
        print(
            'Stack: {}\nPC hand: {}\nTurn: {}'
            .format(
                len(self.stack), len(self.PC.hand), self.turn))

        print('\nTable:')
        for bone in loc_table or self.table:
            print(bone, end='')

        if self.turn == self.Player1.name:
            print('\n\nYour pieces')
            for i, bone in enumerate(self.Player1.hand, start=1):
                print('{}:{}'.format(i, bone))


if __name__ == "__main__":
    dominoes_game = Dominoes()
