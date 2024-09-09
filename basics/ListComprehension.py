#  list Compreshension is a concise way to create lists.

#  It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
#  The expressions can be anything, meaning you can put in all kinds of objects in lists.
# The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.	
# The list comprehension always returns a result list.

names=["John","Tom","Jerry","Rob","johnny"]
# J_names=[]
# without list comprehension
# for name in names:
#     if 'J' in name:
#         J_names.append(name)

# print(J_names)

# with list comprehension
J_names=[name for name in names if 'J' in name]
print(J_names)
