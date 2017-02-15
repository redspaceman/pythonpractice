# pylint: disable=C0103
# pylint: disable=C0111

#Little different process than while, but more concise (5 lines vs. 7)
for _ in range(3): #should run '_' 3 times
    name = input("What's your name? ")
    print("Hello", name + "!")

print("For loop finished.")

#While loop takes up more lines
counter = 0
while counter < 3: #runs while counter is less than 3, than adds +1 each run
    name = input("What's your name? ")
    print("Hello", name + "!")
    counter = counter + 1

print("While loop finished.")
