
#Disclaimer! All solutions are in the most basic think-able way possible, I have been sick a whole week before the test and haven't had time or energy to study anything, I could have done better, I just didn't <3

#Oppgave 1

inp = input("Insert a text that contains Z here: ")

for i in inp:
    if i >= 'z':
        print(i)
        
#Yeah no, idk, ask me numbers, and then it's easy to just use the max thingy, not letters, idk about letters :3 
       
           
#Oppgave 2

def vinnerlag():
    hjemmelag = str(input("Name for home team here: "))
    bortelag = str(input("Name for home team here: "))
    hjemmemaal = int(input("Points for home team here: "))
    bortemaal = int(input("Points for home team here: "))
    
    
    
    if(hjemmemaal > bortemaal):
        print(hjemmelag + ' vant')
    elif(bortemaal > hjemmemaal):
        print(bortelag + ' vant')
    else:
        print('uavgjort')
        
vinnerlag()

#Do I even need comments here? Even a toddler would understand what this thing means
        
'''
Løsning 2 oppg 2

def vinnerlag(hjemmelag, bortelag, hjemmemaal, bortemaal): 
    if(hjemmemaal > bortemaal):
        print(hjemmelag + ' vant')
    elif(bortemaal > hjemmemaal):
        print(bortelag + ' vant')
    else:
        print('uavgjort')
        
vinnerlag('Blah2', 'Blah', '2', '3')
        
'''

#Oppgave 3

#Maybe here comments are important, pretty much just defined a dcitionary containing 2 rows - By and Pop (population)

storste_by = [
    {'by': 'Oslo', 'pop': 1043168},
    {'by': 'Bergen', 'pop' : 260000},
    {'by': 'Stavanger', 'pop': 230000},
    {'by': 'Trondheim', 'pop': 190000},
    {'by': 'Fredrikstad', 'pop': 120000},
    {'by': 'Drammen', 'pop': 110000},
    {'by': 'Porsgrunn', 'pop': 95000},
    {'by': 'Kristiansand', 'pop': 65000},
    {'by': 'Alesund', 'pop': 55000},
    {'by':'Tonsberg', 'pop': 53000}
]

def skriv_mellom_tall():
    minst = int(input('Minste tall for a soke by: '))
    storst = int(input('Storste tall for a soke by: '))
    for x in storste_by:
        inbygerne = int(x['pop'])
        if(storst > inbygerne > minst):
            print(x['by']) 
            
skriv_mellom_tall()

#Just calculate between the values of two numbers, basic maths
    
#Oppgave 5

def fjern_vokaler():
    setning = str(input('Put in a sentence here: '))
    theotherletters = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
    
    for i in setning:
        for y in theotherletters:
            if y == i:
                print(y)
    
fjern_vokaler()

#Eller 

def fjern_vokaler2():
    setning2 = str(input('Put in a sentence here: '))
    vowels = 'AEIOUaeiou'
    
    for i in setning2:
        for y in vowels:
            if y != i:
                print(i)
    
fjern_vokaler2()

#Find things in text, print things that are both in text and finder, use finder (vowels, otherletters) as a filter

#Oppgave 4

'''

1. Not his work, it's the AI's work, so he didn't learn anything
2. Not fair for the other students that are part of the exam with him

Don't ask me about ethics, if I could use chatgpt here I would have, I won't use my teeth to undo a screw if I have screwdriver, we have tools, we use them, I don't see a surgeon using his bare hands to cut into a patient haha

'''