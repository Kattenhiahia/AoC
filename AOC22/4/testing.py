# Python3 code to demonstrate working of
# Check if one dictionary is subset of other
# Using items() + <= operator

# Initialize dictionaries
test_dict1 = {'gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'CS' : 5}
test_dict2 = {'gfg' : 1, 'is' : 2, 'best' : 3, 'extra':12}

# printing original dictionaries
print("The original dictionary 1 : " + str(test_dict1))
print("The original dictionary 2 : " + str(test_dict2))

# Using items() + <= operator
# Check if one dictionary is subset of other
res = test_dict2.items() <= test_dict1.items()
res2 = test_dict1.items() <= test_dict2.items()

# printing result
print("Does dict2 lie in dict1 ? : " + str(res))
print("Does dict1 lie in dict2 ? : " + str(res2))
