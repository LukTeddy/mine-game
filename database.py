import csv


class Database:
    def __init__(self):
        print("Database Loaded...")

    # Read File
    def read_file(self, dataset):
        csv_list = []
        with open("assets/data/" + dataset + ".csv", 'r') as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                csv_list.append(row)
        return csv_list

    # Create Columns
    def list_column(self, dataset, column):
        csv_list = self.read_file(dataset)
        new_list = []
        for row in csv_list:
            new_list.append(str(row[column]))
            try:
                new_list.remove('')
            except ValueError:
                pass
        return new_list

    def define(self):
        # Win Animation
        win_animation = []
        for i, value in enumerate(self.list_column("animation_positions", 0)):
            x_value, sep, y_value = value.partition(', ')
            win_animation.append([x_value, y_value])
        # Lose Animation
        lose_animation = []
        for i, value in enumerate(self.list_column("animation_positions", 1)):
            x_value, sep, y_value = value.partition(', ')
            lose_animation.append([x_value, y_value])
        # Finish Animation
        finish_animation = []
        for i, value in enumerate(self.list_column("animation_positions", 2)):
            x_value, sep, y_value = value.partition(', ')
            finish_animation.append([x_value, y_value])
        return win_animation, lose_animation, finish_animation
