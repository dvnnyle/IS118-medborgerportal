
#styling ANSI
BOLD = "\033[1m"
RED = "\033[91m" 
RESET = "\033[0m"

print(f"{BOLD}{RED}\nErlings Prosjekt \n{RESET}")
print("Du spiller som Erling, prosjektleder for kommunens nye medborgerportal.")
print("Teamet begynner å møte utfordringer. Du må ta tre viktige valg for å lede dem videre.\n")

print("Tast A eller B for å starte:")
print("A = JA (Start simulasjonen)")
print("B = NEI (Avslutt)")
start_valg = input("\nDitt valg: ").upper()

if start_valg in ['A', 'JA', 'J']:
    print("Flott! La oss begynne!\n")
elif start_valg in ['B', 'NEI', 'N']:
    print("Ingen problem! Ta deg tid når du er klar.")
    exit()
else:
    print("LOL, Du har ikke noe valg. Starter simulasjonen likevel...\n")

