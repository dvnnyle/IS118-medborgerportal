# Intro
print("Velkommen til erlings spill!\n")
print("Du spiller som Erling, prosjektlederen\n")
print("Dette spillet lar deg velge 2 ulike valg hver gang det oppstår noe\n")
print("For å komme videre i spillet må du skrive inn A eller B for å svare\n")
print("Er du klar for å begynne?\n")


# Oppsett if, elif, else for å begynne spillet
svar = input("Skriv JA eller NEI: ").upper()


if svar == "JA":
    print("Herlig, da starter vi!")
elif svar == "NEI":
    print("OK")
    exit()
else:
    print("Du må skrive JA for å begynne")
    exit()


# Konflikt 1
print("\nLevel 1:\n")
print("Silje og Sivert sin uenighet har ført til en personkonflikt, hva vil du gjøre?\n")
print("Silje mener Sivert sin løsning vil hindre innovasjon og låse brukeropplevelsen")
print("Sivert mener Silje sin løsning er urealistisk, usikkert og for kostbar\n")


level1 = input("A) Ta det opp i plenum\nB) Ta det opp privat hver for seg\n").upper()


if level1 == "A":
    konflikt = "åpen"
    print("Du tar det opp i plenum\n")
elif level1 == "B":
    konflikt = "privat"
    print("Du tar det opp hver for seg\n")
else:
    print("Ugyldig svar, systemet velger automatisk alternativ A\n")
    konflikt = "åpen"


# Konflikt 2
print("\nLevel 2\n")
print("Det oppstår spenning mellom Hamdi (kulturavdelingen) og Jabir (brukerrepresentant).")
print("De er uenige om hvordan innbyggerne skal delta i digitale folkemøter.")
print("Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform.")
print("Jabir ønsker et mer åpent system med rom for spontane innspill.\n")


level2 = input("A) Ta initiativ til et felles møte\nB) Avvente og håpe de løser det selv\n").lower()


if level2 == "a":
    dialog = "bedre"
    print("De møter hverandre, og situasjonen blir mykere\n")
elif level2 == "b":
    dialog = "værre"
    print("Situasjonen vokser, og partene er sure på hverandre\n")
else:
    print("Ugyldig svar, systemet velger automatisk alternativ A\n")
    dialog = "bedre"


# Konflikt 3
print("\nLevel 3:\n")
print("Motivasjonen i teamet går gradvis nedover.")
print("Hva vil du gjøre for å styrke teamworket igjen?\n")


level3 = input("A) Sette av tid til relasjonsbygging\nB) Prioritere fremdrift og leveranser\n").lower()


if level3 == "a":
    motivasjon = "høy"
    print("Teamet får mer lyst til å jobbe sammen etter sosiale aktiviteter\n")
elif level3 == "b":
    motivasjon = "lav"
    print("Teamet snakker mindre enn før og samarbeidet svekkes\n")
else:
    print("Ugyldig svar, systemet velger automatisk alternativ A\n")
    motivasjon = "høy"


# Oppsummering
print("\nTakk for at du ville spille! Her kommer resultatene dine:\n")


# Konflikt 1 – Silje og Sivert
if konflikt == "åpen":
    print("Du valgte å ta konflikten opp i plenum. Dette ga åpenhet og en felles problemløsning.")
elif konflikt == "privat":
    print("Du valgte private samtaler. Dette ga rom for ærlighet og ro rundt konflikten.")
else:
    print("Systemet valgte en åpen tilnærming til konflikten.")


# Konflikt 2 – Hamdi og Jabir
if dialog == "bedre":
    print("Du tok initiativ til dialog. Dette styrket samarbeidet mellom Hamdi og Jabir.")
elif dialog == "værre":
    print("Du valgte å avvente, noe som gjorde konflikten større.")
else:
    print("Systemet valgte dialog som løsning.")


# Konflikt 3 – Motivasjon
if motivasjon == "høy":
    print("Du prioriterte relasjonsbygging, som styrket tillit og motivasjon i teamet.")
elif motivasjon == "lav":
    print("Du prioriterte fremdrift, som svekket motivasjonen i teamet.")
else:
    print("Systemet valgte relasjonsbygging for å styrke motivasjonen.")


print("\nTakk for innsatsen, Erling! Du har nå fullført spillet.")





