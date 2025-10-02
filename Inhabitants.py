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

    def get_corals(self) -> int:
        return self.corals

    def set_corals(self, v: int):
        self.corals = v

    def get_fish(self) -> int:
        return self.fish

    def set_fish(self, v: int):
        self.fish = v

    def get_invertebrates(self) -> int:
        return self.invertebrates

    def set_invertebrates(self, v: int):
        self.invertebrates = v
