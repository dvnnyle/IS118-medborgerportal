print("Erlings spill for konflikt håndtering\n")
print("I dette spillet spiller du som Erlend prosjektleder\n")
print("Teamet velger å ha et møte for å diskutere utfordringer som har oppstått i prosjektet\n")
print("I dette spillet går du gjennom 5 scenarioer der du må velge hvordan du vil håndtere konfliktene\n")
print("Skriv A eller B for å velge svar i de forskjellige scenarioene\n")
print("Er du klar for å starte?\n")

svar = input("skriv ja eller nei for å starte spillet").upper()

if svar == "ja":
    print("Herlig! spillet starter nå\n")
elif svar== "nei":
    print("Den er grei, du kan ta spillet når du vil\n")
else:
    print("Ugyldig svar, vennligst skriv ja eller nei\n")

print("\n Scenario 1 \n")
print("En uenighet har opstått mellom to teammedlemmer Silje (Designer) og Sivert (IT-rådgiver) konflikten har utviklet seg fra en sakskonflikt til personkonflikt\n")
print("Siljje mener Sivert sin løsningen vil hindre innovasjon og låse brukeropplevelsen\n")
print("Sivert mener Silje sin løsning er urealistisk, usikkert og for kostbar\n")
print("Hvordan vil du håndtere konflikten?\n")
Scenario1 =input("A: Ta en privat samtale med begge partene for å forstå deres synspunkter og ta en beslutning bastert på hva du tenker er riktig for prosjektet\nB: Ta opp konflikten i et teammøte for åpen diskusjon, flere synspunkter og for å finne en løsning som alle kan akseptere\n").lower()

if Scenario1 == "a":
    konflikt = "privat"
    print("Du velger å ta en privat samtale med begge partene for å forstå deres synspunkter og tar en beslutning bastert på hva du tenker er riktig for prosjektet\n")
elif Scenario1== "b":
    konflikt = "gruppe"
    print("Du velger å ta opp konflikten i et teammøte for åpen diskusjon, flere synspunkter og for å finne en løsning som alle kan akseptere\n")
else:
    print("Ugyldig svar, vennligst skriv A eller B\n")

if konflikt == "privat":
    print("ved å ta en privat samtale fikk du bedre innsikt inn i prosjektet og kunne ta en beslutning basert på dette, men uroen mellom partene forsvant ikke og prosjekt vil ta mye ut av dem begge\n")
elif konflikt == "gruppe":
    print("ved å ta opp konflikten i et teammøte fikk du flere synspunkter og kunne finne en løsning som alle kunne akseptere, dette styrket teamet og prosjektet\n")

print("\n Scenario 2\n")
print("Det har oppstått en konflikt mellom Hamdi (kulturavdelingen) og Jabir (brukerrepresentant) de er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter\n")
print("Hamdi mener at en kontrollert løsning gjennom kommunens eksisterende plattform er best\n")
print("Jabir ønsker et mer åpent, dialogbasert system med rom for spontane innspill fra innbyggerne\n")
print("Uenigheten er foreløpig håndterbart men Erling merker at frustrasjonen øker og at det vil påvirke prosjektet, med en viktig milepæl som nærmer seg med prototypen som må være klar om 3 uker vet Erling at hånderingen av denne konflikten tar prioritet\n")
Scenario2 = input ("A: Funger som megler mellom Hamdi og Jabir, oppmuntre dem til å uttrykke sine bekymringer og jobbe mot en kompromissløsning\nB: Bruke din autoritet som prosjektleder til å ta en endelig beslutning basert på hva du mener er best for prosjektet, dette fører til en klar vei framover, men skaper misnøye mellom personellet\n").lower()

if Scenario2 == "a":
    konflikt2 = "megling"
    print("Du velger å fungere som megler mellom Hamdi og Jabir, oppmuntre dem til å uttrykke sine bekymringer og jobbe mot en kompromissløsning\n")
elif Scenario2 == "b":
    konflikt2 = "autoritet"
    print("Du velger å bruke din autoritet som prosjektleder til å ta en endelig beslutning basert på hva du mener er best for prosjektet\n")
else:
    print("Ugyldig svar, vennligst skriv A eller B\n")

if konflikt2 == "megling":
    print("Ved å fungere som megler mellom Hamdi og Jabir, klarte du å finne en kompromissløsning som begge parter kunne akseptere, dette styrket samarbeidet i teamet og prosjektet\n")
elif konflikt2 == "autoritet":
    print("Ved å bruke din autoritet som prosjektleder til å ta en endelig beslutning, skapte du en klar vei framover for prosjektet, men misnøyen mellom Hamdi og Jabir fortsettet å påvirke teamdynamikken negativt\n")

print("\n Scneario 3 \n")
print("Prosjektet går inn i sluttfasen og du merker motivasjonen i laget faller, hva bør gjøres for å heve motivasjonen i laget under denne viktige fasen av prosjektet?\n")

Scenario3 = input("A: du tilbyr å by hele laget på middag på din regning hvis projektet leveres i tide\nB: du velger å minne laget på viktigheten av deres roller og ansvar i prosjektet og dra frem konsekvensene av å ikke levere i tide").lower()

if Scenario3 == "a":
    konflikt3 = "belønning"
    print("du tilbyr å by hele laget på middag på din regning hvis projektet leveres i tide\n")
elif Scenario3 == "b":
    konflikt3 = "sjefsrolle"
    print("du velger å minne laget på viktigheten av deres roller og ansvar i prosjektet og dra frem konsekvensene av å ikke levere i tide\n")
else: 
    print("Ugyldig svar, venunligst skriv A eller B\n")

if konflikt3 == "belønning":
    print("Ved å tilby en belønning for å levere i tide, økte du motivasjonen i laget betydelig, noe som resulterte i at prosjektet ble levert i tide med høy kvalitet\n")
elif konflikt3 == "sjefsrolle":
    print("Ved å minne laget på deres ansvar og konsekvensene av å ikke levere i tide, klarte du å sikre at prosjektet ble levert i tide, men moralen i laget sank betydelig\n")


sak = (Scenario1, Scenario2, Scenario3)
if sak in [("a","a","a"), ("b","b","b"), ("a","a","b"), ("b","b","a")]:
    print("\n Du håndterte konfliktene på en måte du syntes var riktig, håndteringen førte til at prosjektet ble gjennomført og levert i tide, men noen medlemmer i laget ble utmattet og slitne fra pågående konflikter\n")
elif sak in [("b","a","a")]:
    print("\n Du håndterte konfliktene på en måte som fremmet samarbeid og forståelse i laget, dette førte til at prosjektet ble levert i tide med høy kvalitet og et sterkt team\n")
elif sak in [("a","b","b"), ("a","b","a"), ("b","a","b")]:
    print("\n Du valgte å ta beslutninger som prosjektleder som førte til at prosjektet ble levert i tide men moralen mellom medlemmer var ikke i top og produktet ble ikke levert i topp tilstand\n")


print("\n takk for at du deltok i spillet og håper du lærte noe nyttig om konflikt håndtering!\n")
