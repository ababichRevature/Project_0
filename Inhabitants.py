class Inhabitants:
    def __init__(self, corals: int, fish: int, invertebrates: int):
        self.corals = corals
        self.fish = fish
        self.invertebrates = invertebrates

    def __str__(self):
        return (
            f"Corals: {self.corals}\n"
            f"Fish: {self.fish}\n"
            f"Invertebrates: {self.invertebrates}"
        )

    def get_corals(self):
        return self.corals

    def set_corals(self, v):
        self.corals = v

    def get_fish(self):
        return self.fish

    def set_fish(self, v):
        self.fish = v

    def get_invertebrates(self):
        return self.invertebrates

    def set_invertebrates(self, v):
        self.invertebrates = v
