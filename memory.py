class Memory():
    def __init__(self):
        self.memory = [0,0,0]

    def save(self, value, index):
        self.memory[index] = value

    def load(self, index):
        return self.memory[index]

    def load_all(self):
        return self.memory
