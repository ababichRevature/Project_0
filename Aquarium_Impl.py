import logging
from Inhabitants import Inhabitants
from Aquarium import Aquarium
import Aquarium_Logic as Logic

logging.basicConfig(
    filename="Aquarium_Log.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

def show_aquarium():
    aq = Logic.load_single()
    if aq:
        print(Logic.format_line(aq))

def create_aquarium():
    print(" Create Aquarium ")
    try:
        name = input("Name: ").strip()
        volume = float(input("Volume (gal): ").strip())
        corals = int(input("Corals: ").strip())
        fish = int(input("Fish: ").strip())
        inverts = int(input("Invertebrates: ").strip())
        alk = float(input("Alkalinity (dKH): ").strip())
        ca = float(input("Calcium (ppm): ").strip())
    except ValueError:
        print("Please enter numbers where needed.")
        logging.info("create: bad number input")
        return
    if volume <= 0:
        print("Volume must be more than 0.")
        logging.info("create: invalid volume")
        return
    if corals < 0 or fish < 0 or inverts < 0:
        print("Counts cannot be negative.")
        logging.info("create: negative counts")
        return
    if alk < 0 or ca < 0:
        print("Chemistry values cannot be negative.")
        logging.info("create: negative chemistry")
        return
    aq = Aquarium(
        name=name,
        volume_gal=volume,
        inhabitants=Inhabitants(corals, fish, inverts),
        alk_dkh=alk,
        calcium_ppm=ca,
        day=1,
    )
    Logic.save_single(aq)
    print("Aquarium created.")
    logging.info("create: done")

def update():
    aq = Logic.load_single()
    if not aq:
        print("No aquarium found. Please create one.")
        logging.info("update: no aquarium")
        return
    print("\nPick a field to change\n")
    print()
    print("\t1) Name")
    print("\t2) Volume (gal)")
    print("\t3) Corals")
    print("\t4) Fish")
    print("\t5) Invertebrates")
    print("\t6) Alkalinity (dKH)")
    print("\t7) Calcium (ppm)")
    print("\t8) Back\n")
    while True:
        choice = input("Enter 1-8: ").strip()
        try:
            if choice == "1":
                v = input("New name: ").strip()
                aq.set_name(v)
                break
            elif choice == "2":
                v = float(input("New volume (gal): ").strip())
                if v <= 0:
                    print("Volume must be more than 0.")
                    logging.info("update: invalid volume")
                    continue
                aq.set_volume_gal(v)
                break
            elif choice == "3":
                v = int(input("New corals: ").strip())
                if v < 0:
                    print("Value cannot be negative.")
                    logging.info("update: negative corals")
                    continue
                ih = aq.get_inhabitants()
                ih.set_corals(v)
                aq.set_inhabitants(ih)
                break
            elif choice == "4":
                v = int(input("New fish: ").strip())
                if v < 0:
                    print("Value cannot be negative.")
                    logging.info("update: negative fish")
                    continue
                ih = aq.get_inhabitants()
                ih.set_fish(v)
                aq.set_inhabitants(ih)
                break
            elif choice == "5":
                v = int(input("New invertebrates: ").strip())
                if v < 0:
                    print("Value cannot be negative.")
                    logging.info("update: negative inverts")
                    continue
                ih = aq.get_inhabitants()
                ih.set_invertebrates(v)
                aq.set_inhabitants(ih)
                break
            elif choice == "6":
                v = float(input("New alkalinity (dKH): ").strip())
                if v < 0:
                    print("Value cannot be negative.")
                    logging.info("update: negative alk")
                    continue
                aq.set_alk_dkh(v)
                break
            elif choice == "7":
                v = float(input("New calcium (ppm): ").strip())
                if v < 0:
                    print("Value cannot be negative.")
                    logging.info("update: negative calcium")
                    continue
                aq.set_calcium_ppm(v)
                break
            elif choice == "8":
                logging.info("update: back")
                return
            else:
                print("Please enter 1-8.")
        except ValueError:
            print("Please enter a number.")
            logging.info("update: bad number input")
    Logic.save_single(aq)
    print("Saved changes.")
    logging.info("update: saved")

def water_change():
    aq = Logic.load_single()
    if not aq:
        print("No aquarium found. Please create one.")
        logging.info("water change: no aquarium")
        return
    try:
        g = float(input("Gallons to change: ").strip())
    except ValueError:
        print("Please enter a number.")
        logging.info("water change: bad number input")
        return
    if g < 0:
        print("Please enter a positive number.")
        logging.info("water change: negative input")
        return
    if g > aq.get_volume_gal():
        print("You cannot change more than the tank volume.")
        logging.info("water change: over volume")
        return
    aq2 = Logic.water_change(g)
    if aq2:
        print("Water change done.")
        logging.info("water change: done")

def generate_day():
    aq = Logic.advance_one_day()
    if aq:
        print("One day passed.")
        logging.info("day: advanced")
    else:
        print("No aquarium found. Please create one.")
        logging.info("day: no aquarium")

def main():
    while True:
        choice = input(
            "\n\tChoose an option:\n"
            "\n"
            "\t1) Show aquarium\n"
            "\t2) Create aquarium\n"
            "\t3) Update\n"
            "\t4) Generate day\n"
            "\t5) Water change\n"
            "\t6) Quit\n"
        ).strip()
        if choice == "1":
            show_aquarium()
        elif choice == "2":
            create_aquarium()
        elif choice == "3":
            update()
        elif choice == "4":
            generate_day()
        elif choice == "5":
            water_change()
        elif choice == "6":
            logging.info("quit")
            break
        else:
            print("Please enter 1-6.")
            logging.info("menu: bad choice")

if __name__ == "__main__":
    main()
