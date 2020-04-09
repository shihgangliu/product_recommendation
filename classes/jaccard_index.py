class JaccardIndex:
    def __init__(self, first_shopper_set, second_shopper_set):
        self.first_shopper_set = first_shopper_set
        self.second_shopper_set = second_shopper_set

    def get_value(self):
        shopper_intersection_set = \
            self.first_shopper_set & self.second_shopper_set

        shopper_union_set = \
            self.first_shopper_set | self.second_shopper_set

        return len(shopper_intersection_set) / len(shopper_union_set)
