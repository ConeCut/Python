sommer_ol = [
    { "årstall" : 2004, "vinnertider" : {"100 m" : 10.93, "200 m" : 22.06, "400 m" : 49.41} },
    { "årstall" : 2008, "vinnertider" : {"100 m" : 10.78, "200 m" : 21.74, "400 m" : 49.62} },
    { "årstall" : 2012, "vinnertider" : {"100 m" : 10.75, "200 m" : 21.88, "400 m" : 49.55} },
    { "årstall" : 2016, "vinnertider" : {"100 m" : 10.71, "200 m" : 21.78, "400 m" : 49.44} },
    { "årstall" : 2020, "vinnertider" : {"100 m" : 10.61, "200 m" : 21.53, "400 m" : 48.36} }
]

# Funksjon for å skrive ut vinnertider for en gitt distanse
def skriv_ut_vinnertider(dist):
    for ol in sommer_ol:
        aar = ol["årstall"]
        vinnertid = ol["vinnertider"][dist]
        print(f"{aar} var vinnertiden på {dist} {vinnertid} s.")

# Skrive ut vinnertider for 100 m, 200 m og 400 m
distanser = ["100 m", "200 m", "400 m"]
for dist in distanser:
    skriv_ut_vinnertider(dist)


# Beste tidene i 2020
for ol in sommer_ol:
    if ol["årstall"] == 2020:
        print(f"Beste tider i 2020:")
        for distanse, tid in ol["vinnertider"].items():
            print(f"{distanse}: {tid} s")

# Verste tiden på 200 m
verst_tid_200m = max(sommer_ol, key=lambda ol: ol["vinnertider"]["200 m"])
print(f"\nVerste tid på 200 m var i {verst_tid_200m['årstall']}: {verst_tid_200m['vinnertider']['200 m']} s")
best_tid_200m = min(sommer_ol, key=lambda ol: ol["vinnertider"]["200 m"])
print(f"\nVerste tid på 200 m var i {best_tid_200m['årstall']}: {best_tid_200m['vinnertider']['200 m']} s")