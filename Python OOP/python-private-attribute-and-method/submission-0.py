class PasswordManager:
    def __init__(self, password_string):
        self.__password_string = password_string  
    
    # TODO: Implement the verify_password method
    def verify_password(self, input_string):
        return self.__password_string == input_string



# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
