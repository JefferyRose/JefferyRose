print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

weight = int(input("what is your weight? "))
planet = int(input("What planet are you on? "))

venus_gravity = .91
mars_gravity = .38
jupiter_gravity = 2.34
saturn_gravity = 1.06
uranus_gravity = .92
neptune_gravity = 1.19

# Write an if statement below:

if planet == 1:
    new_weight = weight * venus_gravity
    print(new_weight)
elif planet == 2:
    new_weight = weight * mars_gravity
    print(new_weight)
elif planet == 3:
    new_weight = weight * jupiter_gravity
    print(new_weight)
elif planet == 4:
    new_weight = weight * saturn_gravity
    print(new_weight)
elif planet == 5:
    new_weight = weight * uranus_gravity
    print(new_weight)
elif planet == 6:
    new_weight = weight * neptune_gravity
    print(new_weight)
else:
    print("unsported planet")