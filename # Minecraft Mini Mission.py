# Minecraft Mini Mission

# Function for placing steps
def place_steps(step):

    # Places the step 5 times
    for step in range(step):

        # Prints the steps
        print("Place STEP")
    print("Stairs complete!")

# Call back the function
step=int(input("How many steps do you want to place down: "))
place_steps(step)

print("")
print("")

# Function for placing torches
def place_torches(place):

    # Add the torches
    for position in range(place):
        print("Placing torch at position", position)

        # Every 5 torches it says something
        if position % 5 == 0:
            print("Extra bright torch!")
            print("")
            
# Call back the torch function
place=int(input("How many torches do you want to place: "))
place_torches(place)

def build_guard_tower(floor, block):
    for i in range(floor):
        print("Floor", i + 1, "!")
        for i in range(block):
            print("Block", i + 1)
            if i % 5 == 0:
                print("torch", i + 1)

# Call back
floor = int(input("How many floors do you want: "))
block = int(input("How many blocks per floor: "))

build_guard_tower(floor, block)

print("")
print("")

# Building a wall
def build_reinforced_wall(place):
    for i in range(place):
        if i % 4 == 0:
            print("COBBLESTONE AT POSITION", i)
        elif i % 5 ==0:
            print("Defense checkpoint reached at position", i)
            print("")
        else:
            print("PLANK AT POSITION", i)

# Call back plus defining variables
place = int(input("How long do you want your wall to be: "))

build_reinforced_wall(place)

print("")
print("")

# Making night patrol
def night_patrol(time, energy):
    while time > 0:
        print("Patrolling... MINUTE", time)
        time+=1

        if energy < 0:
            energy=0
        print("ENERGY LEVEL:", energy)
        if energy <= 30:
            print("Warning: Low Power")
        if energy <= 0:
            print("Shut down...")
            break
        energy-=12

# Callback
energy=int(input("What's your energy level: "))
time=1
night_patrol(time, energy)