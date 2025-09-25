from collections import deque

print("=== Task 1: Stack Operations ===")

# Simulating Stack (LIFO)
stack = []

# Pushing Steps
stack.append("Step1")
print("Pushed:", stack)
stack.append("Step2")
print("Pushed:", stack)
stack.append("Step3")
print("Pushed:", stack)

# Undo last (Pop)
removed = stack.pop()
print(f"Undo Last (Popped '{removed}'):", stack)

print("\nFinal Stack Content:", stack)


print("\n=== Task 2: Queue Operations ===")

# Simulating Queue (FIFO)
queue = deque()

# 7 Citizens queue
citizens = ["Citizen1", "Citizen2", "Citizen3", "Citizen4", "Citizen5", "Citizen6", "Citizen7"]
for citizen in citizens:
    queue.append(citizen)
    print(f"Enqueued: {citizen} --> Queue: {list(queue)}")

# 3 are served (Dequeue)
for i in range(3):
    served = queue.popleft()
    print(f"Served (Dequeued): {served} --> Queue: {list(queue)}")

# Who is now at the front?
print("\nNow at Front of Queue:", queue[0])
