import math
from operator import itemgetter


class ClosestPair(object):
    def closest_pair_1d_brute_force(self, array):
        closest_distance = 9999999

        for p1 in array:
            for p2 in array:
                if p1 != p2 and abs(p1 - p2) < closest_distance:
                    closest_distance = abs(p1 - p2)

        return closest_distance

    def closest_pair_1d_divide_conquer(self, array):
        sorted_array = sorted(array)
        return self.closest_pair_1d_recursive(sorted_array)

    def closest_pair_1d_recursive(self, array):
        n = len(array)
        if n <= 3:
            return self.closest_pair_1d_brute_force(array)

        mid = int(n / 2)
        left_closest_distance = self.closest_pair_1d_recursive(array[:mid])
        right_closest_distance = self.closest_pair_1d_recursive(array[mid:])
        split_closest_distance = abs(array[mid] - array[mid - 1])
        return min([left_closest_distance, right_closest_distance, split_closest_distance])

    def distance(self, p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    def closest_pair_2d_brute_force(self, array):
        closest_distance = self.distance(array[0], array[1])

        for p1 in array:
            for p2 in array:
                if p1 != p2 and self.distance(p1, p2) < closest_distance:
                    closest_distance = self.distance(p1, p2)

        return closest_distance

    def sort_list_of_lists_by_n_index(self, array, n):
        return sorted(array, key=itemgetter(n))

    def closest_pair_2d_divide_conquer(self, array):
        array_x = self.sort_list_of_lists_by_n_index(array, 0)
        array_y = self.sort_list_of_lists_by_n_index(array, 1)
        return self.closest_pair_2d_recursive(array_x, array_y)

    def closest_pair_2d_recursive(self, array_x, array_y):
        n = len(array_x)

        if n <= 3:
            return self.closest_pair_2d_brute_force(array_x)

        mid = int(n / 2)
        left_x = array_x[:mid]
        right_x = array_x[mid:]
        # Dividing point in the X array
        divide = array_x[mid - 1][0]

        left_y = []
        right_y = []
        for pair_of_coords in array_y:
            if pair_of_coords[0] <= divide:
                left_y.append(pair_of_coords)
            else:
                right_y.append(pair_of_coords)

        left_closest_distance = self.closest_pair_2d_recursive(left_x, left_y)
        right_closest_distance = self.closest_pair_2d_recursive(right_x, right_y)
        closest_distance = min([left_closest_distance, right_closest_distance])

        # Create strip
        strip = []
        for pair_of_coords in array_y:
            if abs(pair_of_coords[0] - divide) < closest_distance:
                strip.append(pair_of_coords)

        # Compare points in strip to points within closest distance below it
        return_value = {}
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1]) < closest_distance:
                distance = self.distance(strip[i], strip[j])
                if distance < closest_distance:
                    closest_distance = distance
                j = j + 1

        return closest_distance

    def parse_text_file(self, path):
        with open(path) as text:
            lines = text.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].replace('\n', '')
                point = lines[i].split(',')
                point[1] = point[1].replace(' ', '')
                point[0] = float(point[0])
                point[1] = float(point[1])
                lines[i] = point
        return lines


    def closest_pair_2d_divide_conquer_allow_duplicate_x(self, array):
        array_x = self.sort_list_of_lists_by_n_index(array, 0)
        array_y = self.sort_list_of_lists_by_n_index(array, 1)
        return self.closest_pair_2d_recursive_allow_duplicate_x(array_x, array_y)


    def closest_pair_2d_recursive_allow_duplicate_x(self, array_x, array_y):
        n = len(array_x)

        if n <= 3:
            return self.closest_pair_2d_brute_force(array_x)

        mid = int(n / 2)
        left_x = array_x[:mid]
        right_x = array_x[mid:]
        # Dividing point in the X array
        divide = array_x[mid - 1]

        left_y = []
        right_y = []
        for pair_of_coords in array_y:
            if pair_of_coords[0] == divide[0]:
                if pair_of_coords[1] <= divide[1]:
                    left_y.append(pair_of_coords)
                else:
                    right_y.append(pair_of_coords)
            elif pair_of_coords[0] <= divide[0]:
                left_y.append(pair_of_coords)
            else:
                right_y.append(pair_of_coords)

        left_closest_distance = self.closest_pair_2d_recursive(left_x, left_y)
        right_closest_distance = self.closest_pair_2d_recursive(right_x, right_y)
        closest_distance = min([left_closest_distance, right_closest_distance])

        # Create strip
        strip = []
        for pair_of_coords in array_y:
            if abs(pair_of_coords[0] - divide[0]) < closest_distance:
                strip.append(pair_of_coords)

        # Compare points in strip to points within closest distance below it
        return_value = {}
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1]) < closest_distance:
                distance = self.distance(strip[i], strip[j])
                if distance < closest_distance:
                    closest_distance = distance
                j = j + 1

        return closest_distance