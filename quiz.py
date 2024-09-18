import csv

filnavn = "spm.csv"

try: 

    with open(filnavn, mode="r", encoding="utf-8") as fil:
    
        spm = []
        svar = []
        next(fil)  # Hopper over første linje
    
        for linje in fil:
            data = linje.strip().split(",")
            spm.append(data[0])
            svar.append(data[1])
    
        for i in range(len(spm)):
            print(f"{i + 1}. Spørsmålet er {spm[i]}")
            print(f"Svaret er {svar[i]}")
            
except Exception as e:
    print("Something Something " + e.__class__.__name__)
    print(e)