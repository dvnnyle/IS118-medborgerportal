
print(" 🎮 Erlings Prosjekt 🎮")
print("Du spiller som Erling, prosjektleder for kommunens nye medborgerportal.")
print("Teamet begynner å møte utfordringer. Du må ta fem viktige valg for å lede dem videre.\n")
print("Skriv 'A' eller 'B' for hvert valg.\n")


print("Er du klar?")
svar = input("👉 Skriv JA eller NEI: ").upper()

if svar == "JA":
    print("Flott! La oss begynne! 🎉\n")
elif svar == "NEI":
    print("Ingen problem! Ta deg tid når du er klar. 😊")
    exit()
else:
    print("Ugyldig svar. Starter spillet likevel... 😈\n")


print("🚀 Level 1: \n")
print("Silje (designer) og Sivert (IT-rådgiver) er uenige om teknologivalg.")
level1 = input("A) Tar det opp i plenum\nB) Snakker med dem hver for seg\n> ").lower()

if level1 == "a":
    konflikt = "åpen"
    print("Du tar det opp i plenum. Stemningen er spent, men ærlig.")
elif level1 == "b":
    konflikt = "rolig"
    print("Du snakker med dem individuelt. Konflikten roer seg litt.")
else:
    print("Ugyldig valg! Velger automatisk A.")
    konflikt = "åpen"

print("\n🚀 Level 2: \n")
print("Hamdi og Jabir er uenige om hvordan innbyggerne skal delta.")
level2 = input("A) Kaller inn til møte\nB) Avventer situasjonen\n> ").lower()

if level2 == "a":
    dialog = "bedre"
    print("Møtet hjelper, de forstår hverandre bedre.")
elif level2 == "b":
    dialog = "verre"
    print("Du venter, og spenningen mellom dem øker.")
else:
    print("Ugyldig valg! Velger automatisk A.")
    dialog = "bedre"

print("\n🚀 Level 3: \n")
print("Du merker at motivasjonen synker i teamet.")
level3 = input("A) Arrangerer sosial kveld\nB) Fokuserer på leveranser\n> ").lower()

if level3 == "a":
    motivasjon = "høy"
    print("Teamet får ny energi og samarbeidet styrkes.")
elif level3 == "b":
    motivasjon = "lav"
    print("Prosjektet går fremover, men folk virker slitne.")
else:
    print("Ugyldig valg! Velger automatisk A.")
    motivasjon = "høy"

print("\n🚀 Level 4: \n")
print("Kommunedirektøren etterspør rask fremdrift.")
level4 = input("A) Lover rask leveranse\nB) Forklarer at kvalitet tar tid\n> ").lower()

if level4 == "a":
    press = "høyt"
    print("Teamet føler press, men jobber hardt for å levere.")
elif level4 == "b":
    press = "balansert"
    print("Du står for kvalitet. Kommunen forstår, men vil se resultater snart.")
else:
    print("Ugyldig valg! Velger automatisk A.")
    press = "høyt"

print("\n🚀 Level 5: \n")
print("Et nytt medlem foreslår endringer i designet.")
level5 = input("A) Åpner for nye ideer\nB) Holder fast på planen\n> ").lower()

if level5 == "a":
    innovasjon = "åpen"
    print("Teamet liker at du er fleksibel. Nye ideer skaper engasjement.")
elif level5 == "b":
    innovasjon = "lukket"
    print("Du holder prosjektet på sporet, men noen føler seg oversett.")
else:
    print("Ugyldig valg! Velger automatisk A.")
    innovasjon = "åpen"




if konflikt == "åpen" and motivasjon == "høy":
    print("Teamet blomstrer! Prosjektet går videre med sterkt samarbeid og tillit.")
elif konflikt == "rolig" and press == "høyt":
    print("Prosjektet leveres, men folk er slitne og samarbeidet er svakt.")
elif dialog == "bedre" and innovasjon == "åpen":
    print("Teamet jobber godt sammen og er åpne for nye ideer.")
elif dialog == "verre" and motivasjon == "lav":
    print("Det er spenninger i teamet, og motivasjonen er lav.")
elif press == "balansert" and innovasjon == "lukket":
    print("Prosjektet leveres i god kvalitet, men uten store innovasjoner.")
elif motivasjon == "høy" and press == "høyt":
    print("Teamet er motivert men stresset av høye forventninger.")
else:
    print("Teamet gjør sitt beste, men manglende kommunikasjon fører til utfordringer.")

print("\nTakk for at du spilte Erlings Prosjekt! \n")

print("\nGame Over! GG\n")