def yes_no(prompt)->bool:
    while True:
        svar = input(prompt + " (j/n): ").strip().upper()
        if svar in ['JA', 'J']:
            return True
        if svar in ['NEI', 'N']:
            return False
        print("Ugyldig svar - vennligst svar med 'JA' eller 'NEI'.")

def valg_a_b(prompt):
    while True:
        valg = input(prompt + " (A/B): ").strip().upper()
        if valg in ['A', 'B']:
            return valg
        print("Ugyldig svar - vennligst svar med 'A' eller 'B'.")

print("Interaktiv simulering av konflikthåndtering i prosjektteam.")
print("Du er Erling, prosjektleder for kommunens nye digitale medborgerportal.")

if not yes_no("Vil du starte prosjektet?"):
    print("Ingen problem. Kom tilbake når du er klar.")
    exit()

print("\nKonflikt mellom Silje (designer) og Sivert (IT)")
print("\nValg 1: Silje og Sivert er i konflikt om teknologi.")
valg1 = valg_a_b(
    "A) Ta opp uenigheten i hele teamet slik alle får samme informasjon\n" 
    "B) Ha separate samtaler med Silje og Sivert for å dempe konflikten individuelt\n> ")

print("\nUenighet mellom Hamdi (kulturavedlingen) og Jabir (brukerrepresentant)")
print("\nValg 2: Hamdi ønsker en plattform for innbyggerdialog, mens Jabir foretrekker åpen dialog.")
valg2 = valg_a_b(
    "A) Kall inn til et felles avklaringsmøte for å finne en løsning sammen\n"
    "B) Avvent situasjonen og se om konflikten løser seg selv over tid\n> ")

print("\nMotivasjon i teamet")
print("\nValg 3: Motivasjonen i teamet begynner å falle.")
valg3 = valg_a_b(
    "A) Sett av tid til relasjonsbygging og teambygging\n"
    "B) Prioriter leveranser og fremdrift for å holde fokus på målene\n> ")

utfall = None 
sak = (valg1, valg2, valg3)

if valg1 == "A":
    print("\nDu velger å ta konflikten opp i plenum. Det gir åpenhet og felles informasjon,"
    " men kan øke spenningen i gruppa på kort sikt. ")
else:
    print("\nDu velger individuelle samtaler. Dette kan dempe konflikten raskt mellom de involverte," 
    " men risikerer misforståelser i resten av teamet.")

if valg2 == "A":
    print("\nDu tar initiativ til et felles møte. Det kan bidra til å avklare forventninger "
          "og redusere misforståelser før konflikten eskalerer.")
else:
    print("\nDu velger å avvente. Noen ganger kan konflikter løse seg selv, "
            "men det er en risiko for at situasjonen forverres.")

if valg3 == "A":
    print("\nDu prioriterer relasjoner og teambygging. Dette kan styrke teamets samhold og motivasjon "
          "på lang sikt.")
else:
    print("\nDu fokuserer på leveranser og fremdrift. Det kan gi tydelig fokus på mål, "
            "men risikoen er at slitasje og motivasjonsfall øker over tid.")
    
if sak in [("A", "A", "A")]:
    utfall = "Konfliktene ble håndtert åpent og strukturert, noe som skapte bedre forståelse og trygghet " \
    "i teamet. Relasjonsfokuset bidro til økt motivasjon, og teamet beveger seg tydelig inn i en norming-fase. "\
    "Prosjektet leverer en solid prototype innen fristen og samarbeidsklimaet er sterkt."
elif sak in [("B", "A", "A")]: 
    utfall = "Individuelle samtaler bidro til å redusere konfliktnivået mellom Silje og Sivert. " \
    "Fellesmøtet mellom Hamdi og Jabir hjalp til med å avklare uenigheter."\
    "Motivasjonen øker, og teamet jobber godt videre, selv om enkelte relasjoner fortsatt krever litt oppfølging."
elif sak in [("A", "A", "B"), ("A", "B", "A"), ("B", "B", "A"), ("A", "B", "B")]:
    utfall = "Noen utfordringer ble håndtert, mens andre forble uavklarte. Dette gir en ujevn teamdynamikk, "\
    "og motivasjonen varierer. Prosjektet går fremover, men samarbeidet er til tider ustabilt på grunn "\
    "av manglende strukturer og tydelige forventningsavklaringer."
elif sak in [("B", "A", "B")]:
    utfall = "Selv om det ble gjennomført et avklaringsmøte, førte valgene dine til økt arbeidsbelastning og redusert motivasjon. "\
    "Konflikten mellom Silje og Sivert er dempet, men teamet er preget av stress. Prosjektet går videre, "\
    "men uten et robust samarbeidsgrunnlag."
elif sak in [("B", "B", "B")]:
    utfall = "Ved å avvente begge konfliktene og samtidig prioritere leveranser over relasjoner, "\
        "blir både kommunikasjon og motivasjon svekket. Teamet forblir i en storming-fase, og ulmende konflikter får vokse. "\
        "Prosjektet står i fare for å stagnere dersom tydelige tiltak settes inn."
else:
    utfall = "Prosjektet viser blandede tendenser. Teamet kommer videre, men det er fortsatt flere utfordringer knyttet til kommunikasjon,"\
    "rolleavklaring og forventningsstyring. Videre ledelse bør fokusere på relasjoner og felles forståelse for å sikre fremdrift."

print("\nSluttresultat:")
print(utfall)
print("\nTakk for at du deltok i simuleringen av Erling sitt prosjekt!.")
