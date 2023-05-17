lst = [(1, 2), (5, 7), (3, 6), (1, 2)]  #list of tuples
print(list(set([i for i in lst])))#inner list loop in the set will remove the duplicates and returns the values in list as per outer list



"""
output:
[(1, 2), (5, 7), (3, 6)]
"""