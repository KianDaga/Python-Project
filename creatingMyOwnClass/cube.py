class Cube:

    def __init__ (self, colour, stickerless, solved, assembled):
        self.colour = colour
        self.stickerless = stickerless
        self.solved = solved
        self.assembled = assembled

    def scramble(self, solved):
        solved = False
        print("You have scrambled the cube")

    def solve(self, solved):
        solved = True
        print("You have solved the cube")

    def assemble(self, assembled):
        assembled = True
        print("You have assembled the cube")

    def disassemble(self,assembled):
        assembled = False
        print("You have disassembled the cube")     


