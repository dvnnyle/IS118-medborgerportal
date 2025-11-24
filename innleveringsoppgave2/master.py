
#ANSI-stiler for farger og tekstformatering i teminalen
BOLD = "\033[1m"
RED = "\033[91m" 
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"


# Funksjon som håndterer ja/nei-spørsmål og ugyldig input
def ja_nei(prompt)->bool:
    while True:
        svar = input(prompt + f"Tast inn: {BOLD}ja{RESET} eller {BOLD}nei{RESET}: ").strip().upper()
        
        if svar in ['JA', 'J']:
            return True
        if svar in ['NEI', 'N']:
            return False
            
        print(f"{BOLD}{RED}\nUgyldig svar - vennligst svar med 'JA' eller 'NEI'.\n{RESET}")

# Funksjon som håndterer A/B-valg og ugyldig input
def valg_a_b(prompt):
    while True:
        valg = input(prompt + "\nTast inn: A eller B:").strip().upper()
        
        if valg in ['A', 'B']:
            print()
            return valg
            
        print(f"{BOLD}{RED}\nUgyldig svar - vennligst svar med 'A' eller 'B'.\n{RESET}")

def spill():

        print("\n---------------")   # --- SPILL STARTER ---
    
    # --- Situasjon 1: Konflikt mellom Silje og Sivert ---
        print(F"{BOLD}{YELLOW}\nSituasjon #1: {RESET}")
    
        print("Silje (designer) og Sivert (IT-rådgiver) er uenige om teknologivalg og design. Konflikten har eskalert fra en sakskonflikt til en personkonflikt.")
        print("Silje mener løsningen til Sivert vil låse brukeropplevelsen og hindre innovasjon.")
        print("Sivert mener Silje ikke forstår de tekniske begrensningene og at hennes forslag er urealistiske og for kostbart.\n")
        print("Erling må ta en beslutning for å håndtere konflikten mellom Silje og Sivert. Han kan velge å ta det opp i plenum eller snakke med dem hver for seg.\n")
    
        print(f"{BOLD}Hva velger du å gjøre?{RESET}")
    
        valg1 = valg_a_b(
            "A) Tar det opp i plenum og finner ut av det sammen\n" 
            "B) Ha separate samtaler med Silje og Sivert for å dempe konflikten individuelt\n"
            )
    
        if valg1 == "A":
            konflikt = "åpen"    # Konfliktstatus brukes i sluttresultatet og score
            print(
                "Du tar det opp i plenum. Stemningen er spent, men alle får samme informasjon.\n"
            )
        else:
            konflikt = "dempet"    # Konfliktstatus brukes i sluttresultatet og score
            print(
                "Du snakker med dem individuelt. Konflikten roer seg litt mellom de involverte.\n"
            )
    
    # --- Situasjon 2: Lavmælt konflikt mellom hamdi og Jabir ---
        print(F"{BOLD}{YELLOW}\nSituasjon #2: {RESET}")
    
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
            dialog = "bedre"    # Dialogutvikling brukes i sluttresultatet og score
            print(
                "Du tar initiativ til et felles møte. Det bidrar til å avklare forventninger og redusere misforståelser.\n"
            )
        else:
            dialog = "forverret"    # Dialogutvikling brukes i sluttresultatet og score
            print(
                "Du velger å avvente. Noen ganger kan konflikter løse seg selv, men det er en risiko for at situasjonen forverres.\n"
            )
    
    # --- Situasjon 3: Valg om motivasjon og arbeidsprioritering ---
        print(F"{BOLD}{YELLOW}\nSituasjon #3: {RESET}")
    
        print("Motivasjonen til flere på teamet begynner å synke.")
        print("Hallgeir ønsker mer sosialt innad i teamet for å skape bedre samhold.")
        print("Silje synes at arbeidet bør prioriteres for å få fullført prosjektet.")
        print("Erling må bestemme om det viktigste er å få motivasjonen opp på teamet eller om arbeidet må prioriteres.\n")
    
        print(f"{BOLD}Hva velger du å gjøre?{RESET}\n")
    
        valg3 = valg_a_b(
            "A) Velg å motiver teamet med en belønning hvis arbeidet blir gjort og levert til fristen\n"
            "B) Velg å minne teamet på rollene de spiller i teamet og at det er en jobb hvor prosjektet må prioriteres over annet\n"
            )
    
        if valg3 == "A":
            motivasjon = "høy"    # Motivasjonsnivået brukes i sluttresultatet og score
            print(
                "Du velger å motivere teamet med en mulig belønning dersom dere leverer produktet i tide med god kvalitet.\n"
                "Dette fører til høyere arbeidsmoral og en sosial helhet innen teamet, hvor de alle jobber mot ett mål.\n"
            )
        else:
            motivasjon = "lav"    # Motivasjonsnivået brukes i sluttresultatet og score
            print(
                "Du velger å følge Siljes synspunkt og prioriterer arbeid over det sosiale.\n"
                "Det fungerer, og arbeidet blir gjort, men du merker at spenningen er høy og at teamet har lav moral.\n"
            )
    
        print("\n---------------")
    
    # Kombinerer valgene til en tuple som brukes for å bestemme sluttuttfall
        utfall = None
        kombinasjon = (valg1, valg2, valg3)
    
    # Bestem sluttutfall basert på kombinasjonene fra de tre valgene
        if kombinasjon in [("A", "A", "A"), ("B", "A", "A")]:
            utfall = (
                f"{GREEN}Konflikten er {konflikt}, dialogen ble {dialog}, og motivasjonen er {motivasjon}.{RESET}\n"
                "Du tok gode valg som førte til samhold i teamet, og at prosjektet ble gjennomført i tide og i god kvalitet.\n"
                "Du lytter til teamet og ser hver del av konfliktene, du viser god lederevne og teamet avslutter prosjektet med høy moral og en følelse av felles mestring."
            )
    
        elif kombinasjon in [("A", "A", "B"), ("A", "B", "A"), ("A", "B", "B"), ("B", "B", "A")]:
            utfall = (
                f"{RED}Konflikten er {konflikt}, dialogen ble {dialog}, og motivasjonen er {motivasjon}.{RESET}\n"
                "Du tok beslutninger basert på magefølelsen din. Dette førte til at prosjektet ble levert i tide, men ikke uten problemer på veien.\n"
                "Konflikter og diskusjoner innen teamet førte til lav moral og forsinkelser. "
            )
    
        else: # Gjenværende kombinasjoner("B", "B", "B"), ("B", "A", "B")
            utfall = (
                f"{RED}Konflikten er {konflikt}, dialogen ble {dialog}, og motivasjonen er {motivasjon}.{RESET}\n"
                "Du velger å ta konflikter opp mellom partiene involvert istedenfor i plenum og noen ganger satser du på at konflikter kan løse seg selv.\n"
                "Dette fører til at teamet i sin helhet mister tillit til hverandre og til deg som leder, og at konfliktene forblir uløste.\n" 
                "Prosjektet leveres riktignok i tide, men kvaliteten er langt under forventningene, og moralen i teamet er svært lav."
            )
    
     # --- ENDING: RESULTATER ---
        print(f"{BOLD}\nSluttresultat: {RESET}\n")
        print(utfall)
        print("\nTakk for at du spilte vårt spill om konflikthåndtering under ett prosjekt!\n")
    
    # --- Scoring beregning basert på konflikt, dialog og motivasjon ---
        score = 0
        if konflikt == "dempet":
            score += 1
    
        if dialog == "bedre":
            score += 1
    
        if motivasjon == "høy":
            score += 1
    
    
        print(f"\n{BOLD}Din Score: {score} av 3{RESET}")
        if score == 3: #max score
            print("Bra jobbet! du har navigert gjennom simulasjonen suksessfullt og tatt gode valg underveis! 🌟")
    
        elif score == 2: #god score
            print("Ikke verst! men det er rom for forbedring. Prøv igjen for å forbedre scoren din!")
    
        else: 
            score == 0 or 1 #lav score
            print ("Du gjorde ditt beste. Hver leder lærer av sine erfaringer er du klar til å prøve igjen?")
    
        print("\n---------------\n")

    # --- Hovedprogram / Restart loop ---

print(f"{BOLD}{GREEN}\nErlings Prosjekt \n{RESET}")
print("Du spiller som Erling, prosjektleder for kommunens nye medborgerportal.")
print("Teamet begynner å møte utfordringer. Du må ta tre viktige valg for å lede dem videre.\n")


if not ja_nei("Vil du starte prosjektet?\n"):
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

while True:
    spill()

    if not ja_nei("Ønsker du å spille igjen?\n"):
        print("Takk for at du spilte! Ha en fin dag!")
        break
 

     # --- SLUTT ---
