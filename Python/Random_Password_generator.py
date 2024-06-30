import random

class InvalidPasswordLength(Exception):
    pass

def generate_password():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()_-+={[}]|:;'<,>.?/"

    while True:
        try:
            pass_len = int(input("Enter the length of the password:"))
            if 8 <= pass_len <= 16:
                password = ""
                password += characters[random.randint(0, 25)]
                password += characters[random.randint(26, 51)]
                password += characters[random.randint(52, 61)]
                password += characters[random.randint(62, 91)]

                for i in range(1, pass_len - 3):
                    password += characters[random.randint(0, 91)]

                pass_list = list(password)
                random.shuffle(pass_list)
                password = ''.join(pass_list)
                return password
            else:
                raise InvalidPasswordLength("Password length must be between 8 and 16 characters!")
        except ValueError:
            print("Invalid input. Please enter a valid integer for password length.")
        except InvalidPasswordLength as e:
            print(e)

if __name__ == "__main__":
    newPassword = generate_password()
    print(f"Random generated password: {newPassword}")
