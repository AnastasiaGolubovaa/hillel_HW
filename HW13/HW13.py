class Human:
    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "phone": self.phone,
            "address": self.address
        }

    def call(self, phone_number):
        print(f"{self.phone} calling {phone_number}")

person1 = Human("John", "Smith", 30, "123456789", "123  St")
person2 = Human("Jane", "Ostin", 25, "987654321", "456 St")
person3 = Human("Guy", "Ritchie", 40, "11111", "789 Ave")

print(person1.get_info())
print(person2.get_info())
print(person3.get_info())
