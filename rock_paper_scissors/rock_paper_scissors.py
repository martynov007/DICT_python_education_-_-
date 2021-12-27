from json.decoder import JSONDecodeError
import random
from pathlib import Path
import json


class Gesture():
    gestures = []

    def __init__(self, title) -> None:
        self.title = title
        self.beat = []
        self.gestures.append(self)

    def add_gesture(self, gesture):
        self.beat.append(gesture)

    @staticmethod
    def get(_k):
        for gest_ in Gesture.gestures:
            if gest_.title == _k:
                return gest_

        return None


class Player:
    def __init__(self) -> None:
        self.name = input('Enter your name: ')
        self.rating = self.get_rating()

    def get_rating(self):
        file = Path('rock_paper_scissors/rating.json')
        rating = None

        if not file.exists():
            file.touch()

        self.file = file

        with file.open('r') as file:
            try:
                data = json.load(file)
                data_rating = data.get(self.name)
            except JSONDecodeError:
                pass

            if rating:
                rating = data_rating
            else:
                rating = 0

        return rating

    def choose_gesture(self, playin_gestures, input_gest):
        while True:
            for gest_ in playin_gestures:
                if input_gest == gest_.title:
                    self.gesture = gest_
                    return
            else:
                print('Error: There is no that gesture')
                input_gest = input('What\'s your gesture ?:')

    def increase_rating(self, points):
        with self.file.open('r') as fl_r:
            try:
                data = json.load(fl_r)
            except JSONDecodeError:
                pass

        with open(self.file, 'w') as fl_a:
            try:
                data.update({self.name: self.rating + points})
                self.rating += points
            except Exception:
                data = {self.name: self.rating + points}
            finally:
                json.dump(data, fl_a)


class RockPaperScissors15:
    base_gestures = [
            'rock', 'fire', 'scissors', 'snake', 'human',
            'tree', 'wolf', 'sponge', 'paper', 'air',
            'water', 'dragon', 'devil', 'lightning', 'gun'
        ]
    playin_gestures = []

    def __init__(self) -> None:
        self.init_gestures()

        playin_gestures = input('Write gestures that you want to play: ')
        self.pick_playin_gestures(playin_gestures)

        if not self.playin_gestures:
            print('Game cant start, there is no playing gestures')
            return

        player = Player()

        while True:
            command = input('')
            if command[0] == '!':
                match command:
                    case '!exit':
                        break
                    case '!rating':
                        print('Your rating is {}'.format(player.rating))
                    case _:
                        print('There is no command {}'.format(command))
            else:
                player.choose_gesture(self.playin_gestures, command)
                self.compete(player)

    def choose_pc_gesture(self):
        return random.choice(self.playin_gestures)

    def compete(self, player):
        pc_gesture = self.choose_pc_gesture()

        if pc_gesture.title in player.gesture.beat:
            print('You won!')
            player.increase_rating(100)
        elif pc_gesture.title == player.gesture.title:
            print('It\'s draw')
            player.increase_rating(50)
        else:
            print('You lost!')

        print('PC choice was: {}'.format(pc_gesture.title))

    def pick_playin_gestures(self, playing_gestures):
        for gest_ in playing_gestures.split(','):
            cl_gest = Gesture.get(gest_)
            if cl_gest:
                self.playin_gestures.append(cl_gest)
            else:
                print('There is no gesture {}'.format(gest_))

    def init_gestures(self):
        for i, gesture in enumerate(self.base_gestures):
            gesture_ = Gesture(gesture)

            for beat_gesture in range(i+1, i+8):

                if beat_gesture == len(self.base_gestures):
                    for beat_gesture in range(0, i - 7):
                        gesture_.add_gesture(self.base_gestures[beat_gesture])

                    break

                gesture_.add_gesture(self.base_gestures[beat_gesture])


if __name__ == "__main__":
    RockPaperScissors15()
