t1 = 3879513793.149376869
t2 = 3879513790.695286751
t3 = 3879513790.715286732
t4 = 3879513793.409376621

delay = ((t4-t1) - (t3-t2))
print(f"delay = {delay}")
offset = (0.5*((t2-t1) + (t3-t4)))
# print(f"offset = {offset}")
print(f"offset magnitude = {abs(offset)}")