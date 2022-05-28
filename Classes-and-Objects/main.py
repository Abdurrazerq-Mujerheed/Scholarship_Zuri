class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        print("My name is ", name)
    
    def change_age(self, age):
        print("My age is ", int(age))
    
    def add_track(self, track):
        print("New track added was ", self.tracks.append(track))
    
    def get_score(self):
        print("The score is ", self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
