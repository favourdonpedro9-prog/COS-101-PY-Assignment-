# COS 101 ASSIGNMENT
# PROGRAM TO SOLVE FIVE PHYSICS FORMULAS

print("====================================")
print("       PHYSICS FORMULA SOLVER")
print("====================================")

while True:
    print("\nSelect a physics formula to solve:")
    print("1. Speed = Distance / Time")
    print("2. Force = Mass * Acceleration")
    print("3. Weight = Mass * Gravity")
    print("4. Density = Mass / Volume")
    print("5. Kinetic Energy = 1/2 * Mass * Velocity²")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ").strip()

    if choice == "6":
        print("Exiting program. Goodbye!")
        break

    try:
        if choice == "1":
            distance = float(input("Enter distance (m): "))
            time = float(input("Enter time (s): "))

            if time != 0:
                speed = distance / time
                print("Speed =", speed, "m/s")
            else:
                print("Error: Time cannot be zero.")

        elif choice == "2":
            mass = float(input("Enter mass (kg): "))
            acceleration = float(input("Enter acceleration (m/s²): "))

            force = mass * acceleration
            print("Force =", force, "Newtons")

        elif choice == "3":
            mass = float(input("Enter mass (kg): "))
            gravity = float(input("Enter gravity (m/s²): "))

            weight = mass * gravity
            print("Weight =", weight, "Newtons")

        elif choice == "4":
            mass = float(input("Enter mass (kg): "))
            volume = float(input("Enter volume (m³): "))

            if volume != 0:
                density = mass / volume
                print("Density =", density, "kg/m³")
            else:
                print("Error: Volume cannot be zero.")

        elif choice == "5":
            mass = float(input("Enter mass (kg): "))
            velocity = float(input("Enter velocity (m/s): "))

            kinetic_energy = 0.5 * mass * velocity ** 2
            print("Kinetic Energy =", kinetic_energy, "Joules")

        else:
            print("Invalid choice. Please select between 1 and 6.")

    except ValueError:
        print("Error: Please enter valid numeric values only.")