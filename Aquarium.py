from Inhabitants import Inhabitants

class Aquarium:
    def __init__(
        self,
        name: str,
        volume_gal: float,
        inhabitants: Inhabitants,
        alk_dkh: float,
        calcium_ppm: float,
        day: int = 1,
    ):
        self.name = name
        self.volume_gal = volume_gal
        self.inhabitants = inhabitants
        self.alk_dkh = alk_dkh
        self.calcium_ppm = calcium_ppm
        self.day = day

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Volume: {self.volume_gal:.1f} gal\n"
            f"Day: {self.day}\n"
            f"Alkalinity: {self.alk_dkh:.2f} dKH\n"
            f"Calcium: {self.calcium_ppm:.0f} ppm\n"
            f"Inhabitants ->\n{self.inhabitants}"
        )

    def get_name(self):
        return self.name

    def set_name(self, v):
        self.name = v

    def get_volume_gal(self):
        return self.volume_gal

    def set_volume_gal(self, v):
        self.volume_gal = v

    def get_inhabitants(self):
        return self.inhabitants

    def set_inhabitants(self, v: Inhabitants):
        self.inhabitants = v

    def get_alk_dkh(self):
        return self.alk_dkh

    def set_alk_dkh(self, v):
        self.alk_dkh = v

    def get_calcium_ppm(self):
        return self.calcium_ppm

    def set_calcium_ppm(self, v):
        self.calcium_ppm = v

    def get_day(self):
        return self.day

    def inc_day(self, n=1):
        self.day += n
