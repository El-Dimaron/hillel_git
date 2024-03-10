import random
import string

# Note: please do not use pass_length higher than 30, as the password might run out of unique elements and the function will display an error

def password_gen(*, letters=True, symbols=False, numbers=False, duplicates=False, pass_length=8):
    if pass_length < 8:
        print("Please be advised that the password has to at least 8 symbols long. Please enter a bigger number.")
    else:
        # Distribution logic - will determine how many elements from each list (letters, symbols, numbers) should be added to make up for a set pass_length
        # The more conditions (arguments True) set by user, the more types of elements should be added to the final password
        number_of_divisions = 0
        conditions_list = [letters, symbols, numbers]
        for condition_ in conditions_list:
            if condition_:
                number_of_divisions += 1

        if number_of_divisions != 0:
            distribution = pass_length // number_of_divisions
            additional_sum = pass_length - (distribution * number_of_divisions)
            letters_distr = distribution + additional_sum
        else:
            letters_distr = pass_length

        password = []

        # Now the function will create separate lists for each element (letters, symbols, numbers).
        # The number of elements in each list will depend on the argumental condition (True/False) and on the required length of password.
        # Finally, all the lists will be added together and shuffled to make up for a final password (password_final), which will be returned by function and also displayed for user's convenience.

        letters_list = []
        if letters:
            letter_elements = string.ascii_letters
        else:
            letter_elements = string.ascii_lowercase

        if duplicates:
            letter_elements_list = []
            for element in letter_elements:
                letter_elements_list.append(element)
            for random_letter in range(letters_distr):
                letters_list.append(letter_elements_list.pop(random.randint(0, len(letter_elements_list) - 1)))
        else:
            for random_letter in range(letters_distr):
                letters_list.append(random.choice(letter_elements))

        # Following block of code is used if no uppercase letter was added (due to random), then the function will add it manually
        if letters:
            if "".join(letters_list).islower():
                letters_list.pop()
                if duplicates:
                    letters_list.append(letter_elements_list[random.randint(0, len(letter_elements_list) - 1)].upper())
                else:
                    letters_list.append(random.choice(string.ascii_uppercase))
        # print(f"letters_list: {letters_list}")

        symbols_list = []
        symbols_to_be_used = "!@#$%^&*()+"
        symbols_to_be_used_list = []
        if symbols:
            if duplicates:
                for symbol in symbols_to_be_used:
                    symbols_to_be_used_list.append(symbol)
                for random_symbol in range(distribution):
                    symbols_list.append(symbols_to_be_used_list.pop(random.randint(0, len(symbols_to_be_used_list) - 1)))
            else:
                for random_symbol in range(distribution):
                    symbols_list.append(random.choice("!@#$%^&*()+"))
            # print(f"symbols_list: {symbols_list}")

        numbers_list = []
        numbers_to_be_used_list = []
        if numbers:
            if duplicates:
                for number in range(0, 10):
                    numbers_to_be_used_list.append(number)  # just numbers from 0 to 9
                for random_number in range(distribution):
                    numbers_list.append(numbers_to_be_used_list.pop(random.randint(0, len(numbers_to_be_used_list) - 1)))
            else:
                for random_number in range(distribution):
                    numbers_list.append(random.randint(0, 10))
            # print(f"numbers_list: {numbers_list}")

        password = letters_list + symbols_list + numbers_list
        random.shuffle(password)
        password_final = ""
        for element in password:
            password_final += str(element)
        print(f"Your password is: {password_final}")
        return password_final

password_gen()
        # displaying all the arguments just to visually compare the difference:
# password_gen(letters=False, symbols=False, numbers=False, duplicates=False, pass_length=8)
# password_gen(letters=True, symbols=False, numbers=False, duplicates=False, pass_length=14)
# password_gen(letters=True, symbols=True, numbers=False, duplicates=False, pass_length=20)
# password_gen(letters=True, symbols=True, numbers=True, duplicates=False, pass_length=24)
# password_gen(letters=True, symbols=True, numbers=True, duplicates=True, pass_length=30)
