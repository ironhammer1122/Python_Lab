# Q1
set_x = {5, 15, 25, 35, 45}
print("Q1 - Set elements:", set_x)

# Q2
values = {5, 10, 15, 20}
values.add(25)
print("Q2 - Updated set:", values)

# Q3
fruits = {"Apple", "Mango", "Banana", "Orange"}
fruits.remove("Mango")
print("Q3 - Updated set:", fruits)

# Q4
group_a = {2, 4, 6, 8}
group_b = {6, 8, 10, 12}
union_set = group_a.union(group_b)
print("Q4 - Union:", union_set)

# Q5
group_c = {10, 20, 30, 40}
group_d = {30, 40, 50, 60}
common_set = group_c.intersection(group_d)
print("Q5 - Intersection:", common_set)

# Q6
first_set = {10, 20, 30, 40, 50}
second_set = {20, 40}
diff_set = first_set.difference(second_set)
print("Q6 - Difference:", diff_set)

# Q7
set_p = {1, 3, 5, 7}
set_q = {5, 7, 9, 11}
sym_diff = set_p.symmetric_difference(set_q)
print("Q7 - Symmetric difference:", sym_diff)

# Q8
small_set = {3, 6}
large_set = {3, 6, 9, 12, 15}
print("Q8 - Is subset:", small_set.issubset(large_set))

# Q9
data = [5, 10, 5, 15, 20, 10, 25, 15]
unique_values = set(data)
print("Q9 - Unique elements:", unique_values)
print("Total unique elements:", len(unique_values))
