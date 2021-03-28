import csv

class Bag:
    def get_bag(self):
        ret_list = []
        with open("Values.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                temp_tuple = (row["letter"], row["points"], row["amount"])
                ret_list.append(temp_tuple)

        return ret_list


