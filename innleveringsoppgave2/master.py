
#styling ANSI
BOLD = "\033[1m"
RED = "\033[91m" 
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"

# Funksjon som håndterer ja/nei-spørsmål
def ja_nei(prompt)->bool:
    while True:
        svar = input(prompt + " (j/n): ").strip().upper()
        
        if svar in ['JA', 'J']:
            return True
        if svar in ['NEI', 'N']:
            return False
            
        print(f"{BOLD}{RED}\nUgyldig svar - vennligst svar med 'JA' eller 'NEI'.\n{RESET}")
        
# Funksjon som håndterer A/B-valg og ugyldig input
def valg_a_b(prompt):
    while True:
        valg = input(prompt + "\nVelg: A eller B:\n").strip().upper()
        
        if valg in ['A', 'B']:
            return valg
            
        print(f"{BOLD}{RED}\nUgyldig svar - vennligst svar med 'A' eller 'B'.\n{RESET}")

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
    "B) Ha separate samtaler med Silje og Sivert for å dempe konflikten individuelt\n"
    )

if valg1 == "A":
    konflikt = "åpen"
    print(
        "Du tar det opp i plenum. Stemningen er spent, men alle får samme informasjon."
    )
else:
    konflikt = "rolig"
    print(
        "Du snakker med dem individuelt. Konflikten roer seg litt mellom de involverte."
    )


print(F"{BOLD}\nSituasjon #2: {RESET}\n")

print("Hamdi (kulturavdelingen) og Jabir (brukerrepresentant) er uenige om plattformens funksjoner.")
print("Hamdi ønsker en plattform som fremmer innbyggerdialog og kulturelle arrangementer.")
print("Jabir foretrekker en mer åpen dialogplattform som fokuserer på direkte kommunikasjon mellom innbyggere og kommunen.\n")
print("Erling merker at denne uenigheten begynner å skape spenninger i teamet. Han må bestemme seg for hvordan han skal håndtere situasjonen.\n")

print(f"{BOLD}Hva velger du å gjøre?{RESET}")

valg2 = valg_a_b(
    "A) Kall inn til et felles avklaringsmøte for å finne en løsning sammen\n"
    "B) Avvent situasjonen og se om konflikten løser seg selv over tid\n"
    )

if valg2 == "A":
    dialog = "bedre"
    print(
        "Du tar initiativ til et felles møte. Det bidrar til å avklare forventninger og redusere misforståelser."
    )
else:
    dialog = "verre"
    print(
        "Du velger å avvente. Noen ganger kan konflikter løse seg selv, men det er en risiko for at situasjonen forverres."
    )
    
print(F"{BOLD}\nSituasjon #3: {RESET}\n")

print("Motivasjonen til flere på teamet begynner å synke.")
print("Hallgeir ønsker mer sosialt innad i teamet for å skape bedre samhold.")
print("Silje syntes at arbeidet bør prioriteres for å få fullført prosjektet.")
print("Erling må bestemme om det viktigste er å få motivasjonen opp på teamet eller om arbeidet må prioriteres.\n")

print(f"{BOLD}Hva velger du å gjøre?{RESET}\n")

valg3 = valg_a_b(
    "A) Velg å motiver laget med en belønning hvis arbeidet blir gjort og levert til fristen\n"
    "B) Velg å minne laget på rollene de spiller i laget og at det er en jobb hvor prosjektet må prioriteres over annet\n"
    )

if valg3 == "A":
    motivasjon = "belønning"
    print(
        "Du velger å gi ut sjansen på en belønning hvis laget klarer å levere produktet på tide med god kvalitet, dette fører til høyere arbeidsmoral og en sosial helhet innen laget, hvor de alle jobber mot ett mål."
    )
else:
    motivasjon = "påmminelse"
    print(
        "Du velger å følge Siljes synspunkt og prioriterer arbeid over det sosiale. Det funker og arbeidet blir gjort, men det du merker at spenningen er høy og at laget har lav moral."
    )

print("\n---------------")

# Kombinerer valgene til en tuple som brukes for å bestemme sluttuttfall
utfall = None
kombinasjon = (valg1, valg2, valg3)

if kombinasjon in [("A", "A", "A"), ("B", "A", "A")]:
    utfall = (
        f"{GREEN}Konflikten er {konflikt}, dialogen ble {dialog}, og motivasjonen er {motivasjon}. {RESET}"
        "Du tokk gode valg som førte til samhold i laget og at prosjektet ble gjennomført i tide og i good kvalitet."
        "Du hører på laget ditt og ser hver del av konfliktene, du viser good leder evnje og laget ditt kommer ut av projektet med god moral."
    )

elif kombinasjon in [("A", "A", "B"), ("A", "B", "A"), ("A", "B", "B"), ("B", "B", "A")]:
    utfall = (
        f"{YELLOW}Konflikten er {konflikt}, dialogen ble {dialog}, og motivasjonen er {motivasjon}. {RESET}"
        "Du tokk beslutninger basert på magefølelsen din. Dette førte til at prosjektet ble levert i tide, men ikke uten problemer på veien. "
        "konflikter og diskusjoner innen laget førte til lav moral og forsinkelser. "
    )

else: # kombinasjon in [("B", "B", "B"), ("B", "A", "B")]:
    utfall = (
        f"{RED}Konflikten er {konflikt}, dialogen ble {dialog}, og motivasjonen er {motivasjon}. {RESET}"
        "Du velger å ta konflikter opp mellom partiene involvert istedenfor i plenum og noen ganger satser du på at konflikter kan løse seg selv. "
        "Dette fører til at laget i sin helhet mister tillit til hverandre og at konflikter ikke blir løst. " 
        "Dere klarer fortsatt å få levert i tide, men kvaliteten er langt ifra hvor den kunne hvert og moralen i laget er lav. "
    )


print(f"{BOLD}\nSluttresultat: {RESET}\n")
print(utfall)
print("\nTakk for at du spilte vårt spill om konflikt håndering under ett prosjekt!\n")
print("\nLaget av Jonas, Martin, Danny, Joseph, Niklas og Hans\n")

