import datetime
import time
import math
import random
import uuid
import importlib

from custom_modules import file_operations
from custom_modules import math_operations


def datetime_menu():
    while True:
        print("\n" + "=" * 40)
        print("Datetime and Time Operations Menu:")
        print("1.Display current date and time")
        print("2.Calculate the difference between two dates/times")
        print("3.Format date into custom format")
        print("4.Stopwatch")
        print("5.countdown timer")
        print("6.Back to main menu")

        choice = input("\nEnter your choice (1-6): ")
        print()

        if choice == "1":
            current_datetime = datetime.datetime.now()
            print("Current date and time:", current_datetime)

        elif choice == "2":
            try:
                first = input("Enter the first date (YYYY-MM-DD): ")
                second = input("Enter the second date (YYYY-MM-DD): ")
                print()

                date1 = datetime.datetime.strptime(first, "%Y-%m-%d")
                date2 = datetime.datetime.strptime(second, "%Y-%m-%d")

                difference = abs((date2 - date1).days)
                print("Difference:", difference, "days")

            except ValueError:
                print("Invalid date format. Please enter date in the format YYYY-MM-DD.")

        elif choice == "3":
            try:
                date_input = input("Enter date (YYYY-MM-DD): ")
                print()

                date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d")

                print("Formatted date:", date_obj.strftime("%d-%m-%y"))
                print("Days:", date_obj.strftime("%A"))
                print("Month:", date_obj.strftime("%B"))

            except ValueError:
                print("Invalid date format. Please enter date in the format YYYY-MM-DD.")

        elif choice == "4":
            print("Stopwatch started.")

            start_time = time.perf_counter()

            input("Press Enter to stop the stopwatch...")

            elapsed = time.perf_counter() - start_time

            print()
            print("Elapsed time:", f"{elapsed:.2f} seconds")

        elif choice == "5":
            try:
                seconds = int(input("Enter countdown time in seconds: "))
                print()

                if seconds < 0:
                    print("Please enter a positive number.")
                    continue

                for remaining in range(seconds, 0, -1):
                    print(
                        f"Time remaining: {remaining} seconds",
                        end="\r"
                    )
                    time.sleep(1)

                print("\nTime's up!")

            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


def mathematical_menu():
    while True:
        print("\n" + "=" * 40)
        print("Mathematical Operations Menu:")
        print("1.calculate factorial")
        print("2.solve compound interest")
        print("3.Trigonometric calculations")
        print("4.area of geometric shapes")
        print("5.Back to main menu")

        choice = input("\nEnter your choice (1-5): ")
        print()

        if choice == "1":
            try:
                num = int(input("Enter a number: "))
                print()
                print("Factorial:", math.factorial(num))

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            try:
                principal = float(input("Enter principal amount: "))
                rate = float(input("Enter annual interest rate (in %): "))
                years = float(input("Enter time in years: "))
                print()
                print("Compound Interest:", round(principal * (1 + rate / 100) ** years - principal, 2))

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "3":
            try:
                angle = float(input("Enter angle in degrees: "))
                print()

                result = math_operations.trigonometry(angle)

                print(f"sin({angle}) = {result['sin']:.4f}")
                print(f"cos({angle}) = {result['cos']:.4f}")
                print(f"tan({angle}) = {result['tan']:.4f}")

            except ValueError:
                print("Please enter a valid angle.")

        elif choice == "4":
            try:
                print("1. Circle")
                print("2. Rectangle")
                print("3. Triangle")

                shape = input("\nChoose shape: ")
                print()

                if shape == "1":
                    radius = float(input("Enter radius: "))
                    print()
                    print(
                        "Area of Circle:",
                        math_operations.circle_area(radius)
                    )

                elif shape == "2":
                    length = float(input("Enter length: "))
                    width = float(input("Enter width: "))
                    print()

                    print(
                        "Area of Rectangle:",
                        math_operations.rectangle_area(
                            length, width
                        )
                    )

                elif shape == "3":
                    base = float(input("Enter base: "))
                    height = float(input("Enter height: "))
                    print()

                    print(
                        "Area of Triangle:",
                        math_operations.triangle_area(
                            base, height
                        )
                    )

                else:
                    print("Invalid shape.")

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


def random_menu():
    while True:
        print("\n" + "=" * 40)
        print("Random Data Generation Menu:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice (1-5): ")
        print()

        if choice == "1":
            print("Random Number:", random.randint(1, 100))

        elif choice == "2":
            numbers = [
                random.randint(1, 100)
                for _ in range(5)
            ]

            print("Random List:", numbers)

        elif choice == "3":
            try:
                length = int(input("Enter password length: "))
                print()

                if length <= 0:
                    print("Length must be greater than 0.")
                    continue

                characters = (
                    "abcdefghijklmnopqrstuvwxyz"
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    "0123456789!@#$%^&*"
                )

                password = "".join(
                    random.choice(characters)
                    for _ in range(length)
                )

                print("Generated Password:", password)

            except ValueError:
                print("Please enter a valid length.")

        elif choice == "4":
            otp = random.randint(100000, 999999)
            print("Generated OTP:", otp)

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


def uuid_menu():
    print("\n" + "=" * 40)
    print("Generate Unique Identifiers (UUID)")
    print()
    print("Generated UUID:", uuid.uuid4())


def file_menu():
    while True:
        print("\n" + "=" * 40)
        print("File Operations (Custom Module) Menu:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice (1-5): ")
        print()

        if choice == "1":
            filename = input("Enter file name: ")
            print()
            print(file_operations.create_file(filename))

        elif choice == "2":
            filename = input("Enter file name: ")
            data = input("Enter data to write: ")
            print()

            print(
                file_operations.write_file(
                    filename, data
                )
            )

        elif choice == "3":
            filename = input("Enter file name: ")
            print()
            print(file_operations.read_file(filename))

        elif choice == "4":
            filename = input("Enter file name: ")
            data = input("Enter data to append: ")
            print()

            print(
                file_operations.append_file(
                    filename, data
                )
            )

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


def explore_module():
    print("\n" + "=" * 40)
    print("Explore Module Attributes (dir())")

    module_name = input(
        "\nEnter module name to explore: "
    )
    print()

    try:
        module = importlib.import_module(module_name)

        attributes = dir(module)

        print(
            f"Available Attributes in {module_name}:"
        )
        print(attributes)

    except ModuleNotFoundError:
        print("Module not found.")


def main():
    while True:
        print("\n==============================")
        print("Welcome to Multi-Utility Toolkit")
        print("==============================")

        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            datetime_menu()

        elif choice == "2":
            mathematical_menu()

        elif choice == "3":
            random_menu()

        elif choice == "4":
            uuid_menu()

        elif choice == "5":
            file_menu()

        elif choice == "6":
            explore_module()

        elif choice == "7":
            print("\n==============================")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("==============================")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()