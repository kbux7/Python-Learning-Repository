class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f"Hey {self.name} darling. You are {self.age} years old right?.")
 
c1 = cat("Feona", 3)
c1.meow()