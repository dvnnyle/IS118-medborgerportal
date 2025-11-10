def intro():
    print("🎮 ERLINGS PROSJEKT 2.0 🎮")
    print("Du spiller som Erling, prosjektleder for kommunens nye medborgerportal.")
    print("Du skal ta fem valg som påvirker prosjektets utvikling.\n")

    svar = input("👉 Er du klar? Skriv JA eller NEI: ").strip().upper()
    if svar == "NEI":
        print("Ta den tiden du trenger. 😊")
        exit()
    else:
        print("Starter spillet! 🚀\n")


def velg(level_tekst, alternativA, alternativB, variabelnavn):
    print(level_tekst)
    valg = input(f"A) {alternativA}\nB) {alternativB}\n> ").lower()

    if valg == "a":
        print(f"Du valgte A: {alternativA}\n")
        return "A"
    elif valg == "b":
        print(f"Du valgte B: {alternativB}\n")
        return "B"
    else:
        print("Ugyldig valg – velger automatisk A.\n")
        return "A"


def avslutning(resultater):
    print("📊 Prosjektstatus:")
    
    konflikt, dialog, motivasjon, press, innovasjon = resultater

    if konflikt == "A" and motivasjon == "A":
        print("Teamet blomstrer – åpen dialog og god motivasjon fører til et sterkt samarbeid!")
    elif konflikt == "B" and press == "A":
        print("Konflikten holdes lav, men teamet føler press og virker slitne.")
    elif dialog == "A" and innovasjon == "A":
        print("Dialogen forbedres og åpen innovasjon skaper fremdrift!")
    elif dialog == "B" and motivasjon == "B":
        print("Dårlig dialog og lav motivasjon skaper uro i teamet.")
    elif press == "B" and innovasjon == "B":
        print("Kvalitet prioriteres, men innovasjonen mangler.")
    elif motivasjon == "A" and press == "A":
        print("Teamet er motivert, men stresset av høye forventninger.")
    else:
        print("Prosjektet går videre, men kommunikasjonen kunne vært bedre.")

    print("\nTakk for at du spilte Erlings Prosjekt 2.0! 🎉")
    print("Game Over. GG!\n")


# ---------------- HOVEDPROGRAM ----------------

intro()

konflikt = velg(
    "🚀 Level 1:\nSilje og Sivert er uenige om teknologivalg.",
    "Tar det opp i plenum",
    "Snakker med dem hver for seg",
    "konflikt"
)

dialog = velg(
    "🚀 Level 2:\nHamdi og Jabir er uenige om innbyggerdeltakelse.",
    "Kaller inn til møte",
    "Avventer situasjonen",
    "dialog"
)

motivasjon = velg(
    "🚀 Level 3:\nTeamet virker umotivert.",
    "Arrangerer sosial kveld",
    "Fokuserer på leveranser",
    "motivasjon"
)

press = velg(
    "🚀 Level 4:\nKommunedirektøren vil ha rask fremdrift.",
    "Lover rask leveranse",
    "Forklarer at kvalitet tar tid",
    "press"
)

innovasjon = velg(
    "🚀 Level 5:\nNytt teammedlem foreslår designendringer.",
    "Åpner for nye ideer",
    "Holder fast på planen",
    "innovasjon"
)

avslutning((konflikt, dialog, motivasjon, press, innovasjon))
