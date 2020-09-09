notes = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
w_notes = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]


class Note:
    def __init__(self, h, w=False):
        self.index = notes.index(h)
        self.w = w

    def __str__(self):
        if self.w:
            return w_notes[self.index]
        return notes[self.index]


if __name__ == "__main__":
    do_1 = Note("до", False)
    doo = Note("до", True)
    do_2 = Note("до")
    print(do_1, doo, do_2)

    sool = Note("соль", True)
    laa = Note("ля", True)
    print(sool, laa)
