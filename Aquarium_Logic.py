import logging
from Inhabitants import Inhabitants
from Aquarium import Aquarium

logging.basicConfig(
    filename="Aquarium_Log.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

MAIN_FILE = "Aquarium.txt"
NEW_WATER_ALK = 14.0
NEW_WATER_CA = 420.0

def format_line(aq: Aquarium) -> str:
    ih = aq.get_inhabitants()
    return (
        "\n"
        f"Name: {aq.get_name()}\n"
        f"Volume: {aq.get_volume_gal():.1f} gal\n"
        f"Day: {aq.get_day()}\n"
        f"Corals: {ih.get_corals()}\n"
        f"Fish: {ih.get_fish()}\n"
        f"Invertebrates: {ih.get_invertebrates()}\n"
        f"Alkalinity: {aq.get_alk_dkh():.2f} dKH\n"
        f"Calcium: {aq.get_calcium_ppm():.0f} ppm\n"
    )

def parse_line(text: str) -> dict:
    rec = {}
    lines = []
    for l in text.strip().splitlines():
        if l.strip():
            lines.append(l.strip())

    for l in lines:
        if ":" in l:
            k, v = l.split(":", 1)
            k = k.strip()
            v = v.strip()
            if k == "Volume":
                rec["Vol"] = v.split()[0]
            elif k == "Alkalinity":
                rec["ALK"] = v.split()[0]
            elif k == "Calcium":
                rec["Ca"] = v.split()[0]
            else:
                rec[k] = v
    return rec

def dict_to_aquarium(d: dict) -> Aquarium:
    return Aquarium(
        name=d.get("Name", "Untitled"),
        volume_gal=float(d.get("Vol", 0.0)),
        inhabitants=Inhabitants(
            int(d.get("Corals", 0)),
            int(d.get("Fish", 0)),
            int(d.get("Invertebrates", 0)),
        ),
        alk_dkh=float(d.get("ALK", 8.0)),
        calcium_ppm=float(d.get("Ca", 400.0)),
        day=int(d.get("Day", 1)),
    )

def load_single() -> Aquarium | None:
    try:
        with open(MAIN_FILE, "r") as f:
            content = f.read()
            if not content.strip():
                print("File is empty.")
                logging.info("file is empty")
                return None
            aq = dict_to_aquarium(parse_line(content))
            logging.info("loaded aquarium")
            return aq
    except FileNotFoundError:
        print("No aquarium found. Please create one.")
        logging.info("file not found")
        return None
    except Exception as e:
        print("Error")
        logging.info(f"read error: {e}")
        return None

def save_single(aq: Aquarium) -> None:
    try:
        with open(MAIN_FILE, "w") as f:
            f.write(format_line(aq))
        logging.info("saved aquarium")
    except Exception as e:
        logging.info(f"save failed: {e}")


def advance_one_day() -> Aquarium | None:
    aq = load_single()
    if aq is None:
        return None
    vol = aq.get_volume_gal()
    if vol <= 0:
        logging.info("day advance skipped: bad volume")
        return None
    corals = aq.get_inhabitants().get_corals()
    drop_alk = (7 * corals) / vol
    drop_calc = (100 * corals) / vol
    aq.set_alk_dkh(max(0.0, aq.get_alk_dkh() - drop_alk))
    aq.set_calcium_ppm(max(0.0, aq.get_calcium_ppm() - drop_calc))
    aq.inc_day(1)
    save_single(aq)
    logging.info(f"day advanced.")
    return aq

def water_change(gallons: float) -> Aquarium | None:
    aq = load_single()
    if aq is None:
        return None
    vol = aq.get_volume_gal()
    if vol <= 0:
        logging.info("water change skipped: bad volume")
        return None
    if gallons < 0:
        gallons = 0.0
        logging.info("water change: negative set to 0")
    if gallons > vol:
        gallons = vol
        logging.info("water change: capped to volume")
    f = gallons / vol
    alk = aq.get_alk_dkh() * (1 - f) + NEW_WATER_ALK * f
    ca = aq.get_calcium_ppm() * (1 - f) + NEW_WATER_CA * f
    aq.set_alk_dkh(alk)
    aq.set_calcium_ppm(ca)
    save_single(aq)
    logging.info(f"water change: {gallons:.1f} gal")
    return aq
