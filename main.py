from ship import Ship

if __name__ == "__main__":
    with open("example.txt", "r") as input_file:
        n_ships = input_file.readline()
        for i in range(int(n_ships)):
            line = input_file.readline()
            ship_info = line.split(" ")
            ship = Ship(int(ship_info[0]), int(ship_info[1]), float(ship_info[2]))
            for row in range(ship.x):
                row_info = input_file.readline()
                ship.fill_row(row_info, row)

            layer = ship.check_layer()
            while(layer):
                layer = ship.check_layer()
