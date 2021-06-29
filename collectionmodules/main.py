# collection modules

from collections import deque

customq = deque(maxlen=4)
print(customq)
customq.append(1)
customq.append(2)
customq.append(3)
customq.append(4)
print(customq)
customq.append(5)
print(customq)
customq.popleft()
print(customq)
customq.clear()
print(customq)