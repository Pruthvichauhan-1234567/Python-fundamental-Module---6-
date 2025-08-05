# 3. Write a Python program that demonstrates the correct use of indentation, comments, and variables following PEP 8 guidelines.
"""
This program calculates the area of a rectangle
based on user-provided width and height values.
It demonstrates proper indentation, comments, and variable naming
according to PEP 8 guidelines.
"""

def calculate_rectangle_area(width, height):
    """
    Calculate the area of a rectangle.

    Parameters:
    width (float): The width of the rectangle
    height (float): The height of the rectangle

    Returns:
    float: The area of the rectangle
    """
    area = width * height
    return area


def main():
    """Main function to run the area calculation."""
    
    # Prompt the user for input
    try:
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Calculate area
    rectangle_area = calculate_rectangle_area(width, height)

    # Display result
    print(f"The area of the rectangle is {rectangle_area:.2f} square units.")


if __name__ == "__main__":
    main()

