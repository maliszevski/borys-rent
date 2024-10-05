class User:
    users = []
    def __init__(self, name, surname, age, e_mail, phone_num):
        self.name = name
        self.surname = surname
        self.age = age
        self.e_mail = e_mail
        self.phone_num = phone_num

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Surname: {self.surname}\n"
                f"Age: {self.age}\n"
                f"E-mail: {self.e_mail}\n"
                f"Phone number: {self.phone_num}")


    def create_and_add_user(self):
        new_user = User(self.name, self.surname, self.age, self.e_mail, self.phone_num)
        User.users.append(new_user)


    def add_users(self, user):
        self.users.append(user)






