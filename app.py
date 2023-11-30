try:
    result = 5 + "hello"
except TypeError as e:
    print(f"Caught an exception: {e}")
except Exception as e:
    print(f"Caught a general exception: {e}")
finally:
    print("This will always run.")
    

def get_user_input():
    while True:
        user_input = input("Please enter a number: ")
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Call the function two times and store the results into two different variables
result1 = get_user_input()
result2 = get_user_input()

# Add these two variables together and print out the result
try:
    total_result = result1 + result2
    print(f"The sum of {result1} and {result2} is: {total_result}")
except TypeError:
    print("Error: Unable to add the results. Please make sure the inputs are valid numbers.")

# Add, commit, and push
# Your version control commands here
