import Soloist
import output


def main():

    test = Soloist.Soloist("iisa0b7e9fu89y98tynqrtypty9tt treugwhv ty a7fgy fgs uilfseuif hasuifyzsufg seufysucfzugishnfzdgfuzsyfusgfuscf u", 0)
    music = test.get_song()
    for sound in music:
        print(sound)
    output.playaudio(music)


main()
