#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211_Assignment7 - The Game of PIG"""

import argparse
import random

random.seed(0)


class Die:
    def __init__(self):
        self.values = [1, 2, 3, 4, 5, 6]

    def roll_a_die(self):
        random.shuffle(self.values)
        return self.values[0]


class Player:
    def __init__(self, player_number):
        self.player_number = player_number
        self.score = 0

    def increase_score(self, new_score):
        self.score += new_score


class Game:
    def __init__(self, num_of_players):
        self.players = []
        self.die = Die()
        for i in range(num_of_players):
            self.players.append(Player(i + 1))

        self.turn = 0

    def is_current_player_wins(self):
        if self.players[self.turn].score >= 100:
            return True
        else:
            return False

    def print_turn_choices_menu(self):
        print("")
        print("Player", self.turn + 1, " Score :", self.players[self.turn].score)
        print("(h) Hold Current Score\n(r) Roll a Die\nChoice:", end='')

    def play(self):
        while self.players[self.turn].score < 100:
            self.print_turn_choices_menu()
            choice = input("")
            if choice == 'h':
                self.turn = (self.turn + 1) % len(self.players)
                print("You chose to Hold with score:", self.players[self.turn].score)
            else:
                print("Rolling a Die...")
                score = self.die.roll_a_die()
                print("You Get ", score)
                if score == 1:
                    print("it's Next Player Turn:")
                    self.turn = (self.turn + 1) % len(self.players)
                else:
                    self.players[self.turn].increase_score(score)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--numPlayers', help='Enter Number of Players')
    parser.add_argument('-c', '--numGames', help='Enter Number of Game')
    args = parser.parse_args()

    games_number = 1
    players_number = 2
    if args.numPlayers:
        players_number = int(args.numPlayers)
    if args.numGames:
        games_number = int(args.numGames)

    while games_number > 0:
        games_number -= 1
        game = Game(players_number)
        game.play()


main()
