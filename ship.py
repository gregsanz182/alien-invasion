import re


class Command():

    def __init__(self, row, col, scale, name):
        self.min_x = row
        self.min_y = col
        self.max_x = row
        self.max_y = col
        self.area = scale*scale
        self.shoot_pos = 0, 0
        self.name = name

    def add_corner(self, row, col):
        if(row < self.min_x):
            self.min_x = row
        elif(row > self.max_x):
            self.max_x = row

        if(col < self.min_y):
            self.min_y = col
        elif(col > self.max_y):
            self.max_y = col
    
    def calc_area_and_aim(self, scale):
        self.area = ((self.max_x - self.min_x) * (self.max_y - self.min_y) * scale)
        self.shoot_pos = (
            ((self.min_x + self.max_x + 1) * scale)/2,
                        ((self.min_y + self.max_y + 1)*scale)/2
        )
    
    def __repr__(self):
        return "{0}:{1:.3f},{2:.3f}".format(self.name, self.shoot_pos[0], self.shoot_pos[1])

class Ship():

    regexp = re.compile("[a-zA-Z]")

    def __init__(self, x, y, scale):
        self.x = x
        self.y = y
        self.scale = scale
        self.surface = []
        self.commands = {}

    def fill_row(self, row_info, row):
        cols = row_info.replace("\n", "").split(" ")
        self.surface.append(cols)
        for col, value in enumerate(cols):
            if self.regexp.fullmatch(value):
                self.__add_command(row, col, value)

    def __add_command(self, row, col, value):
        command = self.commands.get(value)
        if(command is None):
            self.commands[value] = Command(row, col, self.scale, value)
        else:
            command.add_corner(row, col)
            command.calc_area_and_aim(self.scale)

    def check_layer(self):
        layers_commands = []
        commands_aux = self.commands.copy()
        for command_name, command in commands_aux.items():
            if self.__check_command(command_name, command):
                layers_commands.append(command)
                del self.commands[command_name]

        #sorting by area
        layers_commands = sorted(layers_commands, key=lambda layer: layer.area)
        #sorting by name
        layers_commands = sorted(layers_commands, key=lambda layer: layer.area)

        self.__remove_layer(layers_commands)
        
        return layers_commands

    def __check_command(self, command_name: str, command: Command):
        for i in range(command.min_x, command.max_x+1):
            for j in range(command.min_y, command.max_y+1):
                if self.surface[i][j] not in (command_name, " "):
                    return False
        return True

    def __remove_layer(self, layers_commands):
        for command in layers_commands:
            for i in range(command.min_x, command.max_x+1):
                for j in range(command.min_y, command.max_y+1):
                    if self.regexp.fullmatch(self.surface[i][j]):
                        self.surface[i][j] = " "
