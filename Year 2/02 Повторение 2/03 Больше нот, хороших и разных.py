PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]


class Note:
    def __init__(self, h, is_long=False):
        self.index = PITCHES.index(h)
        self.is_long = is_long

    def __str__(self):
        if self.is_long:
            return LONG_PITCHES[self.index]
        return PITCHES[self.index]


class LoudNote(Note):
    def __init__(self, h, is_long=False):
        super().__init__(h, is_long)

    def __str__(self):
        if self.is_long:
            return LONG_PITCHES[self.index].upper()
        return PITCHES[self.index].upper()


class DefaultNote(Note):
    def __init__(self, h=PITCHES[0], is_long=False):
        super().__init__(h, is_long)


class NoteWithOctave(Note):
    def __init__(self, h, octave, is_long=False):
        super().__init__(h, is_long)
        self.octave = octave

    def __str__(self):
        if self.is_long:
            return LONG_PITCHES[self.index] + f" ({self.octave})"
        return PITCHES[self.index] + f" ({self.octave})"


if __name__ == "__main__":
    print(Note("соль"))

    print(LoudNote(PITCHES[4]))
    print(LoudNote("си", is_long=True))

    print(DefaultNote("ми"))
    print(DefaultNote())
    print(DefaultNote(is_long=True))

    print(NoteWithOctave("ре", "первая октава"))
    print(NoteWithOctave("ля", "малая октава", is_long=True))
