from datetime import datetime

t1 = datetime.strptime("2022/12/08 18:39:53.579782", "%Y/%m/%d %H:%M:%S.%f")
t2 = datetime.strptime("2022/12/08 18:39:54.235095", "%Y/%m/%d %H:%M:%S.%f")
t3 = datetime.strptime("2022/12/08 18:39:54.246416", "%Y/%m/%d %H:%M:%S.%f")
t4 = datetime.strptime("2022/12/08 18:39:53.763062", "%Y/%m/%d %H:%M:%S.%f")

delay = ((t4-t1) - (t3-t2)).total_seconds()
print(f"delay = {delay}")
offset = (0.5*((t2-t1) + (t3-t4))).total_seconds()
# print(f"offset = {offset}")
print(f"offset magnitude = {abs(offset)}")