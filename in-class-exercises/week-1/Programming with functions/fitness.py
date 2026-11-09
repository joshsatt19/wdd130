# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Please enter your gender (M or F): ")
    birth_str = str(input("Enter your birthdate (YYYY-MM-DD): "))
    user_height = float(input("Enter your height in U.S. inches: "))
    user_weight = float(input("Enter your weight in U.S. inches: "))
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age = compute_age(birth_str)
    print(f"Age (years): {age}")
    print(f"Weight: {kg_from_lb(user_weight)}")
    print(f"Height: {cm_from_in(user_height)}")
    print(f"BMI: {body_mass_index(user_weight, user_height)}")
    print(f"BMR: {basal_metabolic_rate(gender, user_weight, user_height, age)}")
    # Print the results for the user to see.
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    age = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        age -= 1

    return age


def kg_from_lb(user_weight):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    weight = user_weight*0.45359237

    return weight


def cm_from_in(user_height):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    height = user_height*2.54

    return height


def body_mass_index(user_weight, user_height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """

    bmi = (10000*user_weight)/(user_height**2)


    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """

    if gender == "M":
        bmr = 88.362 + (13.397*weight) + (4.799*height) - (5.677*age)
    else: gender == "F"
    bmr = 447.593 + 9.247*weight + 3.098*height - 4.330*age

    return bmr


# Call the main function so that
# this program will start executing.
main()