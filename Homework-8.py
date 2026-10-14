class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Yoga Style:", self.yoga_style)
class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        print("Yoga Style:", self.yoga_style)
employee1 = Employee("Rahul", "Staff")
trainer1 = Trainer("Arun", "Trainer", "Weight Training")
yogaInstructor1 = YogaInstructor("Priya", "Yoga Instructor", "Hatha Yoga")
multiTrainer1 = MultiTrainer("Kiran", "Multi Trainer", "Fitness Training", "Vinyasa Yoga")

print("Employee Details:")
employee1.display()

print("Trainer Details:")
trainer1.display()

print("Yoga Instructor Details:")
yogaInstructor1.display()

print("Multi Trainer Details:")
multiTrainer1.display()
