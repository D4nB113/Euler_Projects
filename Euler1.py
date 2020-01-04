from datetime import datetime

now = datetime.now()

total = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i

elapsed =  datetime.now() - now

print(total)
print(elapsed.total_seconds() * 1000)
