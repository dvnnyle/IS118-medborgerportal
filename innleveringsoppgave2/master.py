
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


#TODO LAGE NIVÅER / SITUASJONER

#TODO LAGE ENDINGER BASERT PÅ VALGENE

#TODO EVENTUELT LAGE POENGSYSTEM
=======

print(" Level 1: \n")
print("Konflikt 1: Silje (designer) og Sivert (IT-rådgiver) er uenige teknologivalg og design. Konflikten har eskalert fra en sakskonflikt til en personkonflikt")
print("Silje mener løsningen til Sivert vil låse brukeropplevelsen og hindre innovasjon.")
print("Sivert mener Silje ikke forstår de tekniske begrensningene og at hennes forslag er urealistiske og for kostbart.")
print("Erling må ta en beslutning for å håndtere konflikten mellom Silje og Sivert. han kan velge å ta det opp i plenum eller snakke med dem hver for seg.")
level1 = input("A) Tar det opp i plenum\nB) Snakker med dem hver for seg\n> ").lower()
if level1 == "a":
    konflikt = "åpen"
    print("Du tar det opp i plenum. Stemningen er spent, men roer seg litt men fortsatt spent")
elif level1 == "b":
    konflikt = "rolig"
    print("Du snakker med dem individuelt. Konflikten roer seg litt, men det er enda spenning mellom Silje og Sivert.")
else:
    print("Ugyldig valg! Velger automatisk A.")
    konflikt = "åpen"

print(" Level 2: \n")
print("Konflikt 2: Uenighet mellom Hamdi (kulturavdelingen) og Jabir (brukerrepresentant)")
print("...")
print("...")
print("...")
level2 = input("A) ...nB) ...\n> ").lower()
if level2 == "a":
    dialog = "bedre"
    print("...")
elif level2 == "b":
    dialog = "verre"
    print("...")
else:
    print("Ugyldig valg! Velger automatisk A.")
    konflikt = "bedre"
