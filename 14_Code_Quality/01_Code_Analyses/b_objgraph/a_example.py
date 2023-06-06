"""
Purpose: objgraph

     pip install -U objgraph --user

"""

import objgraph

# print(dir(objgraph))


#Basic Reference Tracking
x = [1, 2, 3]
y = [x, {'a': x}]

objgraph.show_refs([x], filename='ref_graph.png')


objgraph.show_most_common_types()

# -----------------------------
print()


def my_leaky_func():
    pass


# Start counting
objgraph.show_growth(limit=10)


my_leaky_func()

# Stop and show change
objgraph.show_growth(limit=10)
