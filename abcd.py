# File: abc.py

def calculate_square_area(side_length):
    """
    Calculate the area of a square.

    Parameters:
    - side_length (float): The length of one side of the square.

    Returns:
    float: The area of the square.
    """
    area = side_length ** 2
    return area

def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle.

    Parameters:
    - base (float): The length of the base of the triangle.
    - height (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    area = 0.5 * base * height
    return area

def greet_person(name):
    """
    Generate a greeting message for a person.

    Parameters:
    - name (str): The name of the person.

    Returns:
    str: A personalized greeting message.
    """
    greeting = f"Hello, {name}! Welcome!"
    return greeting