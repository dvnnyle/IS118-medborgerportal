
print ("Velkommen til CrewMate Simulator\n")
print("Du er prosjektleder for et viktig kommunalt IT-prosjekt.\n")
print("Teamet ditt består av dyktige, men og kvinner med sterke meninger.\n")
print("Du må ta fem viktige valg for å lede dem videre.\n")
print("Skriv 'A' eller 'B' for hvert valg.\n")
print("Er du klar?")
svar = input(" Skriv JA eller NEI: ").upper()

if svar == "JA":
    print("Flott! La oss begynne!\n")
elif svar == "NEI":
    print("Ingen problem! Ta deg tid når du er klar. 😊")
    exit()
else:
    print("Ugyldig svar.\n")


print(" Level 1: \n")
print("Henriette (designer) og Herman (IT-rådgiver) er uenige om teknologivalg. Hvordan kan vi best løse problemet før det eskalerer?")
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

print("\n Level 2: \n")
print("Ingebritsen og Herman er uenige om hvordan de skal delta. Hva gjør du?")
level2 = input("A) Kaller inn til møte\nB) Avventer situasjonen, og ser hva utfallet blir\n> ").lower()
if level2 == "a":
    dialog = "bedre"
    print("Møtet hjelper, de forstår hverandre bedre.")
elif level2 == "b":
    dialog = "verre"
    print("Du venter, og spenningen mellom dem øker.")
else:
    print("Ugyldig valg! Velger automatisk A.")
    dialog = "bedre"

print("\n Level 3: \n")
print("Du merker at motivasjonen synker i teamet. Hva gjør du?")
level3 = input("A) Arrangerer pizza fest fordi det hjelper alltid\nB) Fokuserer på prosjektet\n> ").lower()
if level3 == "a":
    motivasjon = "høy"
    print("Teamet får ny energi og samarbeidet styrkes.")
elif level3 == "b":
    motivasjon = "lav"
    print("Prosjektet går fremover, men folk virker slitne.")
else:
    print("Ugyldig valg! Velger automatisk A.")
    motivasjon = "høy"
print("\n Level 4: \n")
print("En av teammedlemmene, Herman, virker misfornøyd med arbeidsbelastningen sin. Hva gjør du?")
level4 = input("A) Snakker med ham for å forstå hans bekymringer\n B) Ignorerer det, han må bare takle det\n> ").lower()
if level4 == "a":
    arbeidsbelastning = "forstått"
    print("Herman setter pris på at du tar deg tid til å lytte.")
elif level4 == "b":
    arbeidsbelastning = "misfornøyd"
    print("Herman føler seg oversett og blir mer frustrert. han slutter i jobben og anmelder deg til statsforvalteren")
else:
    print("Ugyldig valg! Velger automatisk A.")
    arbeidsbelastning = "forstått"
print("\n Level 5: \n")
print("Kommunedirektøren etterspør rask fremdrift. Hva sier du?")
level5 = input("A) Lover rask leveranse\nB) Forklarer at kvalitet tar tid\n> ").lower()
if level5 == "a":
    press = "høyt"
    print("Teamet føler press, men jobber hardt for å levere.")
elif level5 == "b":
    press = "balansert"
    print("Du står for kvalitet. Kommunen forstår, men vil se resultater snart.")
else:
    print("Ugyldig valg! Velger automatisk A.")
    press = "høyt"

print("\nTakk for at du spilte CrewMate Simulator! 🎉\n")
if konflikt == "åpen" and dialog == "bedre" and motivasjon == "høy" and arbeidsbelastning == "forstått" and press == "balansert":
    print("Fantastisk jobb! Du har navigert gjennom utfordringene og ledet teamet ditt til suksess! 🌟")
    innovasjon = "åpen"
else:
    print("Du gjorde ditt beste! Hver leder lærer av sine erfaringer. Prøv igjen for å forbedre dine ferdigheter!" )

print ("\nHer er en oppsummering av dine valg:\n")
print(f"Konflikthåndtering: {konflikt}")
print(f"Dialog mellom teammedlemmer: {dialog}")
print(f"Motivasjonsnivå: {motivasjon}")
print(f"Arbeidsbelastning: {arbeidsbelastning}")
print(f"Press fra ledelsen: {press}")

# Beregn poeng: gi poeng for gode valg, trekk for negative valg, og normaliser til 0-5
score = 0
if konflikt == "rolig":
    score += 1
elif konflikt == "åpen":
    score -= 1

if dialog == "bedre":
    score += 1
elif dialog == "verre":
    score -= 1

if motivasjon == "høy":
    score += 1
elif motivasjon == "lav":
    score -= 1

if arbeidsbelastning == "forstått":
    score += 1
elif arbeidsbelastning == "misfornøyd":
    score -= 1

if press == "balansert":
    score += 1
elif press == "høyt":
    score -= 1

# Sikre at score ligger innenfor 0 til 5
score = max(0, min(5, score))

print(f"\nDin poengsum: {score} av 5")

if score == 5:
    print("Fantastisk jobb! Du har navigert gjennom utfordringene og ledet teamet ditt til suksess! 🌟")
elif score >= 3:
    print("Bra jobbet! Du har mange riktige valg, men det er rom for forbedring.")
else:
    print("Du gjorde ditt beste! Hver leder lærer av sine erfaringer. Prøv igjen for å forbedre dine ferdigheter!")
