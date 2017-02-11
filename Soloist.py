import random
import math


class Soloist:

    chrom = [440.00, 466.16, 493.88, 523.25, 554.37, 587.33, 622.25, 659.25, 698.46,
             739.99, 783.99, 830.61, 880.00]
    ratios = [0, 3, 5, 7, 10, 12]

    song = []

    phrases = [[0, 2, 1, 0], [0, 1, 0], [4, 3, 2, 1], [4, 5, 0, 4], [0], [3, 4, 5, 5], [4, 5, 4, 5, 4, 5, 4, 5, 4, 5]]

    h_step = math.pow(2, (1/12))

    def __init__(self, chars, root):
        seg = math.floor(len(chars)/48)
        input = chars[:-(len(chars) % 48)]
        notes = []
        hash = 0
        for ind in range(48):
            for ch in input[ind*seg:len(input) - ind*seg]:
                hash = (hash + ord(ch)) % 6
            notes.append(hash)
        first = self.get_scale(self.chrom[root])
        fourth = self.get_scale(self.chrom[(root + 5) % 12])
        fifth = self.get_scale(self.chrom[(root + 7) % 12])
        #Key of A, start on root
        self.song.append(self.get_phrase(first, root))
        for i in range(len(notes)-1):
            bar = i % 12
            #Assuming that notes is a string of chars 0-6
            if bar < 4 or (bar > 5 and bar < 8) or bar == 10:
                self.song.append(self.get_phrase(first, notes[i]))
            elif bar < 6 or bar == 9:
                self.song.append(self.get_phrase(fourth, notes[i]))
            else:
                self.song.append(self.get_phrase(fifth, notes[i]))
            self.song.append(self.get_phrase(fifth, 0))

    def get_scale(self, root):
        scale = []
        for steps in self.ratios:
            scale.append(root*math.pow(self.h_step, steps))
        print()
        return scale

    def get_song(self):
        return self.song

    def get_phrase(self, mode, inval):
        seq = random.choice(self.phrases)
        phrase = []
        for item in seq:
            if item is None:
                phrase.append(0)
            elif item >= len(mode):
                phrase.append(mode[(item+inval) % len(mode)]*2)
            else:
                phrase.append(mode[(item+inval) % len(mode)])
        return tuple(phrase)