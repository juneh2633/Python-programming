# path = input("과자집에 가는길: ").split(" --> ")
# path.pop() 
# print("우리집에 오는길: " + " --> ".join(path[::-1]) + " --> 우리집")
path_input = input("과자집에 가는길: ").split(" --> ")
stack = []  

for location in path_input:
    if location == "과자집":
        break
    stack.append(location)

print("우리집에 오는길:", end=" ")
while stack:
    print(stack.pop(), end=" --> " if stack else " --> 우리집")
