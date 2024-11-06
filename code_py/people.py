class Human:
    
    def __init__(person, name, surname, age, height, eye_colour, hair_colour, birthday):
        person.name = name
        person.age = age
        person.surname = surname
        person.height = height
        person.eye_colour = eye_colour
        person.haircolour = hair_colour
        person.birthday = birthday
        
    def showPerson(person):
        print(f'Hi, I am {person.name} {person.surname} and Im {person.age}. I am {person.height} tall, I have {person.eye_colour} eyes and my hair is {person.haircolour}. I was born the {person.birthday}')