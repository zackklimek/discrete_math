import unittest

# function converting a python list to a set
def make_set(set):
    new_set = []
    # iterates through set and adds item to the set being returned
    # if it hasn't already been added
    for item in set:
        if item in new_set:
            pass # do nothing - item is not added
        else:
            new_set.append(item)
    # returns the set of the elements passed
    return new_set

# function taking the union of two sets passed as input
def union(set_one, set_two):
    # makes sure the input lists are sets
    set_one = make_set(set_one)
    set_two = make_set(set_two)
    return_set = []
    # adds each item in set_one to return_set
    for item in set_one:
        return_set.append(item)
    # adds each item in set_two to return_set
    for item in set_two:
        return_set.append(item)
    # makes the collection of all of the elements into a set
    return_set = make_set(return_set)
    # returns the union of the sets as a set
    return return_set
            
# function taking the intersection if two sets passed as input
def intersect(set_one, set_two):
    # makes sure the input lists are sets
    set_one = make_set(set_one)
    set_two = make_set(set_two)
    intersect_set = []
    for item in set_one:
        # if item in set_one is in set_two, item is added to set being returned
        if item in set_two:
            intersect_set.append(item)
    # return intersection of the sets as a set
    return intersect_set

# function taking the symmetric difference of two sets passed as input
def symmetric_diff(set_one, set_two):
    # makes sure the input lists are sets
    set_one = make_set(set_one)
    set_two = make_set(set_two)
    diff_set = []
    # any item in set_one that isn't in set_two is added to new set
    for item in set_one:
        if item in set_two:
            pass # do nothing
        else:
            diff_set.append(item)
    # any item in set_two that isn't in set_one is added to new set
    for item in set_two:
        if item in set_one:
            pass
        else:   #do nothing
            diff_set.append(item)
    # return symmetric difference as a set
    return diff_set



class TestSets(unittest.TestCase):
    set_a = ["A", "B", "C", "D", "A"]
    set_b = ["A", "B", "C", "D", "F"]
    set_c = ["C", "D", "E"]

    def test_make_set(self):
        self.assertEqual(make_set(["A", "B", "C", "D", "A"]),
                         ['A', 'B', 'C', 'D'])

    def test_union(self):
        self.assertEqual(union(["A", "B", "C", "D", "F"],["C", "D", "E"]),
                         ['A', 'B', 'C', 'D', 'F', 'E'])

    def test_intersect(self):
        self.assertEqual(intersect(["A", "B", "C", "D", "F"],["C", "D", "E"]),
                         ["C","D"])

    def test_symmetric_diff(self):
        self.assertEqual(symmetric_diff(["A", "B", "C", "D", "F"],["C", "D", "E"]),
                         ['A', 'B', 'F', 'E'])

if __name__ == '__main__':
    unittest.main()
