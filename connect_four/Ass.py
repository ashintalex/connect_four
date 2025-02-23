#Name: Ashin ALex
#ID  : 170238021
#UPI  : atha534

class GameBoard:
    def __init__(self, size):
        self.size = size
        self.num_disks = [0] * size
        self.items = [[0] * size for i in range(size)]
        self.points = [0] * 2

    def num_free_positions_in_column(self, column):
        return self.items[column].count(0)
    
    def game_over(self):
        return all(self.num_free_positions_in_column(col_num) == 0 for col_num in range(len(self.items)))
    
    def display(self):
        symbols = {0: " ", 1: "o", 2: "x"}
        border = "+" + "-" * (self.size * 2 - 1) + "+"
        print(border)
        for row in range(self.size - 1, -1, -1):
            row_str = "|"
            for col in range(self.size):
                row_str += symbols[self.items[col][row]] + " "
            row_str += "|"
            print(row_str)
        print(border)
        print(" ".join(str(val) for val in range(self.size)))
        print(f"Points player 1: {self.points[0]}")
        print(f"Points player 2: {self.points[1]}")
    

    def count_in_direction(self, start_col, start_row, next_col, next_row, player):
        count = 0
        col, row = start_col, start_row
        for i in range(3):
            col += next_col
            row += next_row
            if 0 <= col < self.size and 0 <= row < self.size and self.items[col][row] == player:
                count += 1
        
        return count
    
    def calculate_points(self, points):
        return points - 3

    def num_new_points(self, column, row, player):
        
        points = 0

        left_count = self.count_in_direction(column, row, -1, 0, player)
        right_count = self.count_in_direction(column, row, 1, 0, player)
        if left_count + right_count + 1 >= 4:
            points += self.calculate_points(left_count + right_count + 1)

        up_count = self.count_in_direction(column, row, 0, 1, player)
        down_count = self.count_in_direction(column, row, 0, -1, player)
        if up_count + down_count + 1 >= 4:
            points += self.calculate_points(up_count + down_count + 1)

        diagonal_top_left_count = self.count_in_direction(column, row, -1, 1, player)
        diagonal_bottom_right_count = self.count_in_direction(column, row, 1, -1, player)
        if diagonal_top_left_count + diagonal_bottom_right_count + 1 >= 4:
            points += self.calculate_points(diagonal_top_left_count + diagonal_bottom_right_count + 1)

        diagonal_bottom_left_count = self.count_in_direction(column, row, -1, -1, player)
        diagonal_top_right_count = self.count_in_direction(column, row, 1, 1, player)
        if diagonal_bottom_left_count + diagonal_top_right_count + 1 >= 4:
            points += self.calculate_points(diagonal_bottom_left_count + diagonal_top_right_count + 1)

        return points
        
    
    def add(self, column, player):
        if self.num_free_positions_in_column(column) == 0:
            return False
        row = self.num_disks[column]
        self.items[column][row] = player
        self.num_disks[column] += 1
        self.points[player - 1] += self.num_new_points(column, row, player)
        return True
    
    def free_slots_as_close_to_middle_as_possible(self):
        middle = (self.size - 1)/2 
        free_slots = []
        for i in range(self.size):
            if self.num_free_positions_in_column(i) > 0:
                free_slots.append(i)
        return sorted(free_slots, key=lambda x: (abs(middle - x), x))
    
    def slot_closest_to_middle(self, slots):
        middle = (self.size - 1)/2 
        return sorted(slots, key=lambda x: (abs(middle - x), x))[0]
    
    def column_resulting_in_max_points(self, player):
        max_points = 0
        equal_max_points = []
        for i in range(self.size):
            if self.num_free_positions_in_column(i) > 0:
                row = self.num_disks[i]
                points = self.num_new_points(i, row, player)
                if points > max_points:
                    max_points = points
                    equal_max_points = [i]
                elif points == max_points:
                    equal_max_points.append(i)

        if not equal_max_points:
            return (self.free_slots_as_close_to_middle_as_possible()[0], 0)
        
        if max_points == 0:
            best_slot = self.slot_closest_to_middle(equal_max_points)
        else:
            middle = (self.size - 1 / 2)
            best_slot = min(equal_max_points, key=lambda x: (abs(middle - x), x))
        
        return (best_slot, max_points)




