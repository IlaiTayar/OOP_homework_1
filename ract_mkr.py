class Ract_mkr:

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.box = "[ ]"

    def print_ract(self):
        w_counter = 0
        h_counter = 0
        while True:
            print(self.box, end="")
            w_counter += 1
            if w_counter == self.width:
                print()
                w_counter = 0
                h_counter += 1
            if h_counter == self.height:
                break