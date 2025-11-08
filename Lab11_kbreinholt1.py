import math as m
from fractions import Fraction

"""
        Program: Lab11_kbreinholt1.py
        Author: K-den Breinholt
        Purpose: Takes a numeric string input representing a degree amount of rotation
                 and outputs the equivalent rotation with unnecessary rotations removed.
                 Added an option for outputting the result in radians if desired, and
                 learned ansi escape codes for color coding the output. I know I always
                 say this.. but I had a lot of fun with this one.
        Date: 11-08-25
"""

reset_text = "\033[0m"
red_text = "\033[31m"
green_text = "\033[32m"
yellow_text = "\033[33m"
cyan_text = "\033[36m"
bold_text = "\033[1m"
bold_red_text = "\033[1;31m"
bold_green_text = "\033[1;32m"
bold_cyan_text = "\033[1;36m"

yes_values = {
    "y", "yes", "yeah", "yea", "ye", "yep", "yup", "sure", "ok", "okay", "k", "kk",
    "absolutely", "definitely", "certainly", "affirmative", "of course", "alright",
    "mhmm", "si", "sí", "oui", "ja", "sim", "da"
}
degree_values = {"d", "deg", "degs", "degree", "degrees"}
radian_values = {"r", "rad", "rads", "radian", "radians"}

def degrees_to_radians(degrees):
        """
        Converts an angle from degrees to radians, expressing the result
        in terms of pi when possible.
        Args:
                degrees (float or int): The angle in degrees.

        Returns:
                str: The radian value, expressed in terms of pi if applicable,
                     otherwise as a floating-point number.
        """
        radians = m.radians(degrees)
        pi_fraction = Fraction(radians / m.pi).limit_denominator(1000)
        if abs(pi_fraction.numerator / pi_fraction.denominator - (radians / m.pi)) < 1e-6:
                if pi_fraction.denominator == 1:
                        if pi_fraction.numerator == 0:
                                return "0"
                        elif pi_fraction.numerator == 1:
                                return "π"
                        elif pi_fraction.numerator == -1:
                                return "-π"
                        else:
                                return f"{pi_fraction.numerator}π"
                else:
                        if pi_fraction.numerator == 1:
                                return f"π/{pi_fraction.denominator}"
                        elif pi_fraction.numerator == -1:
                                return f"-π/{pi_fraction.denominator}"
                        else:
                                return f"{pi_fraction.numerator}π/{pi_fraction.denominator}"
        else:
                return f"{radians:.4f}"

def calculate_rotation(degrees_str):
        """
        Converts the given number string to an int and calculates the minimum expression
        for the equivalent rotation in terms of degrees.
        Args:
                degrees_str (str): The given number of degrees as a string.

        Returns:
                degrees (int or None): Degrees of the given rotation adjusted
                                       to remove unnecessary rotations.
                                       (None when given an invalid input)
        """
        try:
                degrees = int(degrees_str)
                return degrees % 360
        except (ValueError, TypeError):
                print(f"\n{bold_red_text}Invalid input:{reset_text} please enter a whole number!\n")
                return None


def main():
        print(f"\n\t{bold_cyan_text}Welcome to the Rotation Calculator!{reset_text}\n")

        while True:
                while True:
                        degrees_str = input(f"{cyan_text}Please give a rotation amount in degrees.\nDegrees:{reset_text} ")
                        result = calculate_rotation(degrees_str)

                        if result is not None:
                                break

                degrees = int(degrees_str)
                while True:
                        unit_type = input(f"\n{cyan_text}Would you like that in Radians or Degrees?\nUnits:{reset_text} ").strip().lower()
                        if unit_type in degree_values or unit_type in radian_values:
                                break
                        else:
                                print(f"\n{red_text}Invalid Input:{reset_text} Would you like that converted into radians, or left as degrees?")
                if unit_type in degree_values:
                        if 0 <= degrees < 360:
                                print(f"\n{bold_green_text}A {degrees}° rotation is already in simplest form.{reset_text}\n")
                        else:
                                print(f"\n{green_text}A {degrees}° rotation is equivalent to {result}°.{reset_text}\n")
                elif unit_type in radian_values:
                        radians = degrees_to_radians(degrees)
                        print(f"\n{green_text}A {degrees}° rotation is equivalent to {radians} radians.{reset_text}\n")
                again = input(f"{yellow_text}Would you like to enter another number?\nAnswer: {reset_text}").strip().lower()
                if again not in yes_values:
                        print(f"\n{bold_cyan_text}Thank you for using the Rotation Calendar.\nGoodbye!\n{reset_text}")
                        break
                else:
                        print()


if __name__ == "__main__":
        main()
