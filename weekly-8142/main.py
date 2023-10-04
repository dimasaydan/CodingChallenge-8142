# Main function
def rintCube(num):
    for i in range(1, num+1):
        print(f"Current Number is : {i} and the cube is {i**3}")

# Input
input_number = int(input("input_number = "))

# Calling function
rintCube(input_number)
