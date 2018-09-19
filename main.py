from ship import Ship

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        n_ships = int(input_file.readline())
        with open("output.txt", "w") as output_file:
            for i in range(n_ships):
                line = input_file.readline()
                ship_info = line.split(" ")
                ship = Ship(int(ship_info[0]), int(ship_info[1]), float(ship_info[2]))
                for row in range(ship.x):
                    row_info = input_file.readline()
                    ship.fill_row(row_info, row)

                layer = ship.check_layer()
                while(layer):
                    output_file.write(
                        ";".join([cmd.get_aim_string() for cmd in layer]))
                    layer = ship.check_layer()
                    if layer: output_file.write(" ")
                
                if i < n_ships+1: output_file.write("\n")
