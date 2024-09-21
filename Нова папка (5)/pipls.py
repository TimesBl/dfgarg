import time     # для засікання часу

class Pupil():

    def init(self,Surname,Name,Mark):
        self.Surname = Surname
        self.Name = Name
        self.Mark = Mark

pupils=[]


def pint_class(pupils):
    for pupil in pupils:
        print(pupil.Surname,pupil.Name,"-",pupil.Mark)
    print("\n")



with open("pipils.txt", "r",encoding= "utf=8") as file:
    for line in file:
        data = line.split(" ")
        pupil = Pupil(data[0], data[1], int(data[2]))
        pupils.append(pupil)