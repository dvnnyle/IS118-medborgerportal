
#styling ANSI
BOLD = "\033[1m"
RED = "\033[91m" 
RESET = "\033[0m"


def ja_nei(prompt)->bool:
    while True:
        svar = input(prompt + " (j/n): ").strip().upper()
        if svar in ['JA', 'J']:
            return True
        if svar in ['NEI', 'N']:
            return False
        print("Ugyldig svar - vennligst svar med 'JA' eller 'NEI'.")

def valg_a_b(prompt):
    while True:
        valg = input(prompt + "\nVelg: A eller B:\n").strip().upper()
        if valg in ['A', 'B']:
            return valg
        print("Ugyldig svar - vennligst svar med 'A' eller 'B'.")


###########

print(f"{BOLD}{RED}\nErlings Prosjekt \n{RESET}")
print("Du spiller som Erling, prosjektleder for kommunens nye medborgerportal.")
print("Teamet begynner å møte utfordringer. Du må ta tre viktige valg for å lede dem videre.\n")


if not ja_nei("Vil du starte prosjektet?"):
    print("Ingen problem. Kom tilbake når du er klar.")
    exit()

print("\n---------------")

#TODO LAGE NIVÅER / SITUASJONER

print(F"{BOLD}\nSituasjon #1: {RESET}\n")

print("Silje (designer) og Sivert (IT-rådgiver) er uenige teknologivalg og design. Konflikten har eskalert fra en sakskonflikt til en personkonflikt.")
print("Silje mener løsningen til Sivert vil låse brukeropplevelsen og hindre innovasjon.")
print("Sivert mener Silje ikke forstår de tekniske begrensningene og at hennes forslag er urealistiske og for kostbart.\n")
print("Erling må ta en beslutning for å håndtere konflikten mellom Silje og Sivert. Han kan velge å ta det opp i plenum eller snakke med dem hver for seg.\n")

print(f"{BOLD}Hva velger du å gjøre?{RESET}")
valg1 = valg_a_b(
    "A) Tar det opp i plenum og finner ut av det sammen\n" 
    "B) Ha separate samtaler med Silje og Sivert for å dempe konflikten individuelt\n")

if valg1 == "A":
    konflikt = "åpen"
    print("Du tar det opp i plenum. Stemningen er spent, men alle får samme informasjon.")
else:
    konflikt = "rolig"
    print("Du snakker med dem individuelt. Konflikten roer seg litt mellom de involverte.")



print(F"{BOLD}\nSituasjon #2: {RESET}\n")

print("Hamdi (kulturavdelingen) og Jabir (brukerrepresentant) er uenige om plattformens funksjoner.")
print("Hamdi ønsker en plattform som fremmer innbyggerdialog og kulturelle arrangementer.")
print("Jabir foretrekker en mer åpen dialogplattform som fokuserer på direkte kommunikasjon mellom innbyggere og kommunen.\n")
print("Erling merker at denne uenigheten begynner å skape spenninger i teamet. Han må bestemme seg for hvordan han skal håndtere situasjonen.\n")

print(f"{BOLD}Hva velger du å gjøre?{RESET}")
valg2 = valg_a_b(
    "A) Kall inn til et felles avklaringsmøte for å finne en løsning sammen\n"
    "B) Avvent situasjonen og se om konflikten løser seg selv over tid\n")
if valg2 == "A":
    dialog = "bedre"
    print("Du tar initiativ til et felles møte. Det bidrar til å avklare forventninger og redusere misforståelser.")
else:
    dialog = "verre"
    print("Du velger å avvente. Noen ganger kan konflikter løse seg selv, men det er en risiko for at situasjonen forverres.")
    
print(F"{BOLD}\nSituasjon #3: {RESET}\n")

#TODO LAGE ENDINGER BASERT PÅ VALGENE

#TODO EVENTUELT LAGE POENGSYSTEM


