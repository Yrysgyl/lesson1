class Employee:
    all_employees = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.all_employees.append(self)

    @classmethod
    def add_employee(cls, name, salary):
        cls.all_employees.append(cls(name, salary))

    @classmethod
    def total_salary(cls):
        total = sum(emp.salary for emp in cls.all_employees)
        return total

    @classmethod
    def average_salary(cls):
        total_employees = len(cls.all_employees)
        if total_employees == 0:
            return 0
        else:
            return cls.total_salary() / total_employees



# Employee.add_employee("John", 50000)
# Employee.add_employee("Alice", 60000)
# Employee.add_employee("Bob", 70000)
#
# print("Total salary of all employees:", Employee.total_salary())
# print("Average salary of all employees:", Employee.average_salary())





class User:
    total_users = 0

    def __init__(self, username, password):
        if self.validate_username(username) and self.validate_password(password):
            self.username = username
            self.password = password
            User.total_users += 1
        else:
            raise ValueError("Invalid username or password")

    def display_info(self):
        print(f"Username: {self.username}")
        print("Password: ********")

    @staticmethod
    def validate_username(username):
        # Имя пользователя должно содержать только буквы и цифры, а также быть не короче 5 символов
        if username.isalnum() and len(username) >= 5:
            return True
        else:
            return False

    @staticmethod
    def validate_password(password):
        # Пароль должен содержать не менее 8 символов
        if len(password) >= 8:
            return True
        else:
            return False


user1 = User("johndoe", "strong_password123")
user2 = User("janesmith", "password_8")

user1.display_info()
user2.display_info()

print(f"Total users created: {User.total_users}")

print("Username validation:", User.validate_username("john_doe"))
print("Password validation:", User.validate_password("strong_password123"))
