# -*- coding: utf-8 -*-
from __future__ import print_function

import random

from beckon import CallbackRegistry


reg = CallbackRegistry()


class Dice(object):

    def __init__(self):
        random.seed()

    def roll(self):
        return random.randint(1, 6)


class DiceRoller(object):

    def __init__(self, nb):
        self._dices = nb

    def roll_all(self):
        dice = Dice()
        return sum([dice.roll() for _ in xrange(self._dices)])


class ResultHandler(object):

    @reg.accept('dice_sum')
    def publish_results(self, result):
        print(result)


class ResultGenerator(object):

    def __init__(self):
        self._roller = DiceRoller(5)

    @reg.emit('dice_sum')
    def generate(self, count):
        for _ in xrange(count):
            yield self._roller.roll_all()


if __name__ == '__main__':
    print('Starting...')
    handler = ResultHandler()
    generator = ResultGenerator()
    generator.generate(10)
    print('Done')
