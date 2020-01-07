add_library('controlP5')

def setup():
    # Globals voor spelers
    global speler1, speler2, speler3, speler4, punten1, punten2, punten3, punten4

    # Globals voor vraag kaart buttons
    global vraagButton, vraagButtonClicked, vraagButtonBack

    # Globals voor pech kaart buttons
    global pechKaartButton, pechKaartButtonClicked, pechKaartButtonBack

    # Globals voor dobbelsteen buttons
    global diceButton, diceButtonClicked, diceButtonBack

    # Globals voor Noord-Amerika
    global NAButton, NAButtonClicked, NAQuestions, NAAnswers

    # Globals voor Zuid-Amerika
    global SAButton, SAButtonClicked, SAQuestions, SAAnswers

    # Globals voor Oceanië/Antarctica
    global OAButton, OAButtonClicked, OAQuestions, OAAnswers

    # Globals voor Azië
    global AZButton, AZButtonClicked, AZQuestions, AZAnswers

    # Globals voor Afrika
    global AFButton, AFButtonClicked, AFQuestions, AFAnswers

    # Globals voor Europa
    global EUButton, EUButtonClicked, EUQuestions, EUAnswers

    # Globals voor overige buttons
    global startButton, startButtonClicked, quitFromGameButton, quitFromMenuButton, showAnswerButton

    # Overige globals
    global cp5, randPechkaart, side, pechIndex, buttonwidthCont, buttonheightCont

    # Globals voor fonts
    global normalTextFont, titleFont, continentButtonFont

    # Define background
    size(1280, 700)
    fill(0)
    background(240)

    # Define fonts
    normalTextFont = createFont("arrial", 30)
    titleFont = createFont("arrial", 80)
    continentButtonFont = createFont("arrial", 30)
    smallButtonFont = createFont("arrial", 25)

    # Define points
    punten1 = 0
    punten2 = 0
    punten3 = 0
    punten4 = 0

    # Define buttons check
    startButtonClicked = False
    diceButtonClicked = False
    vraagButtonClicked = False
    pechKaartButtonClicked = False
    NAButtonClicked = False
    SAButtonClicked = False
    EUButtonClicked = False
    AZButtonClicked = False
    AFButtonClicked = False
    OAButtonClicked = False

    # Define ControlP5 library
    cp5 = ControlP5(this)

    # Define dice
    size(1280, 700)
    pfont = createFont("Arial",20)
    buttonFont = ControlFont(pfont,241)
    side = int(random(1,7))

    # Define pechkaarten
    pechIndex = ['Sla een beurt over (niet vergeten!)',
                'Vlieg terug naar het begin van het vorige continent',
                'Geef een punt aan de volgende speler',
                'Je volgende worp is het aantal stappen dat je terug moet doen in plaats van naar voren',
                '2 punten van je score af',
                '1 punt van je score af']

    # Creating buttons main menu.
    vraagButton = cp5.addButton("Vragen kaart").setValue(0).setPosition(75, 500).setSize(350, 125)
    vraagButton.getCaptionLabel().setFont(buttonFont).setSize(35)
    diceButton = cp5.addButton("Dobbelsteen").setValue(0).setPosition(455, 500).setSize(350, 125)
    diceButton.getCaptionLabel().setFont(buttonFont).setSize(35)
    pechKaartButton = cp5.addButton("Pech kaart").setValue(0).setPosition(835, 500).setSize(350, 125)
    pechKaartButton.getCaptionLabel().setFont(buttonFont).setSize(35)
    quitFromGameButton = cp5.addButton("Spel Afsluiten").setValue(0).setPosition(1050, 30).setSize(200, 70)
    quitFromGameButton.getCaptionLabel().setFont(buttonFont).setSize(20)
    diceButtonBack = cp5.addButton("TERUG").setValue(0).setPosition(455, 500).setSize(350, 125)
    diceButtonBack.getCaptionLabel().setFont(buttonFont).setSize(35)
    vraagButtonBack = cp5.addButton("Terug").setValue(0).setPosition(75, 500).setSize(350, 125)
    vraagButtonBack.getCaptionLabel().setFont(buttonFont).setSize(35)
    pechKaartButtonBack = cp5.addButton("terug").setValue(0).setPosition(835, 500).setSize(350, 125)
    pechKaartButtonBack.getCaptionLabel().setFont(buttonFont).setSize(35)
    showAnswerButton = cp5.addButton("Laat antwoord zien").setValue(0).setPosition(850, 600).setSize(330, 60)
    showAnswerButton.getCaptionLabel().setFont(smallButtonFont).setSize(25)
    startButton = cp5.addButton("Spel Starten").setValue(0).setPosition(455, 300).setSize(350, 125)
    startButton.getCaptionLabel().setFont(buttonFont).setSize(25)
    quitFromMenuButton = cp5.addButton("Afsluiten").setValue(0).setPosition(455, 450).setSize(350, 125)
    quitFromMenuButton.getCaptionLabel().setFont(buttonFont).setSize(25)


    buttonwidthCont = 400
    buttonheightCont = 60
    # Creating continental buttons
    NAButton = cp5.addButton("Noord-Amerika").setValue(0).setPosition(75, 80).setSize(buttonwidthCont,buttonheightCont)
    NAButton.getCaptionLabel().setFont(continentButtonFont).setSize(25)
    SAButton = cp5.addButton("Zuid-Amerika").setValue(0).setPosition(75, 150).setSize(buttonwidthCont,buttonheightCont)
    SAButton.getCaptionLabel().setFont(continentButtonFont).setSize(25)
    EUButton = cp5.addButton("Europa").setValue(0).setPosition(75, 220).setSize(buttonwidthCont,buttonheightCont)
    EUButton.getCaptionLabel().setFont(continentButtonFont).setSize(25)
    AZButton = cp5.addButton("Azie").setValue(0).setPosition(75, 290).setSize(buttonwidthCont,buttonheightCont)
    AZButton.getCaptionLabel().setFont(continentButtonFont).setSize(25)
    AFButton = cp5.addButton("Afrika").setValue(0).setPosition(75, 360).setSize(buttonwidthCont,buttonheightCont)
    AFButton.getCaptionLabel().setFont(continentButtonFont).setSize(25)
    OAButton = cp5.addButton("Oceanie/Antarctica").setValue(0).setPosition(75, 430).setSize(buttonwidthCont,buttonheightCont)
    OAButton.getCaptionLabel().setFont(continentButtonFont).setSize(25)
    NAQuestions = ['Wie is de 45ste president van de Verenigde Staten?\n- Donald Trump\n- Richard Nixon\n- Barack Obama',
                'In welke stad staat het witte huis?\n- Washington D.C\n- New York\n- Sacramento',
                'Hoeveel landen liggen er in Noord-Amerika?\n- 23\n- 24\n- 17',
                'Wat zijn de 3 grootste landen van Noord-Amerika?\n- Canada, De verenigde staten en Mexico\n- Texas, Canada en Florida\n- De verenigde staten, Mexico en Florida',
                'Hoe heette New York vroeger?\n- Nieuw-Amsterdam\n- New Harlem\n- Nieuw-Rotterdam',
                'Wat is de hoofdstad van Canada?\n- Ottawa\n- Sacramento\n- Washington D.C',
                'Hoelang duurt de vlucht van Amsterdam naar New York?\n- Ongeveer 8 uur\n- Ongeveer 9 uur\n- Ongeveer 5 uur',
                'Wat waren de originele bewoners van Noord-Amerika?\n- Aziaten\n- Indianen\n- Mexicanen',
                'Er zijn 2 politieke partijen in Noord-Amerika. Welke zijn dit?\n- Democraten en de Republikeinen\n- Democraten en de Vrijmetselaars\n- Vrijmetselaars en de Vrijheidsstrijders',
                'Wat voor continent ligt er onder Noord-Amerika?\n- Zuid-Amerika\n- Mexico\n- Canada',
                'Vertaal: I am going to work today.\n- Ik ga naar mijn werk vandaag\n- Ik ga naar de kapper vandaag\n- Ik ga naar mijn oma vandaag',
                'Hoeveel sterren staan er op de Amerikaanse vlag?\n- 50\n- 45\n- 51',
                'Waar staan de sterren op de Amerikaanse vlag voor?\n- Het aantal landen in Amerika.\n- Het aantal staten in Amerika.\n- Het aantal presidenten.',
                'Wie was de eerste president van Amerika?\n- George Washington\n- George Bush\n- Bill Clinton']
    NAAnswers = ['Donald Trump',
                'Washington D.C.',
                '23',
                'Canada, De Verenigde Staten en Mexico',
                'Nieuw-Amsterdam',
                'Ottawa',
                'Ongeveer 8 uur',
                'Aziaten',
                'Democraten en Republikeinen',
                'Zuid-Amerika',
                'Ik ga naar mijn werk vandaag',
                '50',
                'Het aantal staten in Amerika',
                'George Washington']

    SAQuestions = ['Wat is het grootste land in Zuid Amerika?\n- Argentinie\n- Peru\n- Brazilie',
                'Door hoeveel landen stroomt de Amazone Rivier?\n- 1, Suriname\n- 2, Brazilie en Suriname\n- 3, Brazilie, Colombia en Peru',
                'Hoe groot is het Amazone Regenwoud?\n- Groter dan 5 miljoen vierkante kilometer\n- 2.5 miljoen vierkante kilometer\n- Kleiner dan 1 miljoen vierkante kilometer',
                'Welke oude groep mensen woonden ooit in Zuid Amerika?\n- Indianen\n- Incas\n- Aboriginals',
                'Welk land ligt niet in Zuid Amerika?\n- Paraguay\n- Nepal\n- Frans Guinea',
                'Welk dier wordt onder andere gevonden in Zuid Amerika?\n- Pinguin\n- Ratelslang\n- Tijger',
                'Wanneer was Zuid Amerika gevonden?\n- 1542\n- 1492\n- 1442']

    SAAnswers = ['Brazilie',
                '3, Brazilie, Colombia en Peru',
                'Groter dan 5 miljoen vierkante kilometer',
                'Incas',
                'Nepal',
                'Pinguin',
                '1492']
    EUQuestions = ['Hoe hoog is de Eiffeltoren?\n- 263 meter\n- 324 meter\n- 337 meter',
                'In welke stad ligt het Colosseum?\n- Rome\n- Venetie\n- Turijn',
                'Waar komen tulpen oorspronkelijk vandaan?\n- Griekenland \n- Nederland\n- Turkije',
                'Welk dier kan je in Europa in het wild spotten?\n- Tijger\n- Walvis\n- Cobra',
                'Wat is het kleinste land in Europa?\n- Vaticaanstad\n- Liechtenstein\n- Monaco',
                'Wat is het grootste land in Europa?\n- Rusland\n- Oekraine\n- Frankrijk',
                'Wat is de grootste berg in Europa?\n- Mount Everest\n- Mount Elbrus\n- Matterhorn',
                'Wat is het voornaamste vervoermiddel in Venetie?\n- Zwemmen\n- Boot\n- Waterfiets',
                'Welk van deze 3 landen gebruikt niet de euro?\n- Denemarken\n- Vaticaanstad\n- San marino',
                'Waar staat Nederland om bekend?\n- Kaas, Klompen, Bergen\n- Kaas, Klompen, Molens\n- Kaas, Klompen, Warm weer',
                'In welk dorp of stad in nederland staan veel molens?\n- Rotterdam\n- Amsterdam\n- Kinderdijk',
                'In welk dorp/stad staat de toren van Pisa?\n- Turijn\n- Rome\n- Pisa',
                'Hoe heet het kleine land tussen Portugal en Spanje?\n- Liechtenstein\n- Andorra\n- San marino',
                'Wat is de vorm van de onderkant van italie?\n- Laars\n- Strijkijzer\n- Boot',
                'Wat staat er op de vlag van Turkije?\n- Zon en maan\n- Halve maan en ster\n- Zon en halve maan',
                'Hoe heet de groep waar de landen van europa samenwerken?\n- Europese Unie\n- Europese Groep\n- Verenigde Naties']
    EUAnswers = ['324 meter',
                'Rome',
                'Turkije',
                'Walvis',
                'Vaticaanstad',
                'Rusland',
                'Mount Elbrus',
                'Boot',
                'Denemarken',
                'Kaas, Klompen, Molens',
                'Kinderdijk',
                'Pisa',
                'Andorra',
                'Laars',
                'Halve maan en ster',
                'Europese Unie']
    AZQuestions = ['Welk land heeft de meeste inwoners ter wereld?\n- China\n- India\n- Rusland',
                'Hoe eet men in India?\n- Met bestek\n- Met hun rechterhand\n- Met stokjes',
                'Hoeveel eilanden heeft Japan?\n- Meer dan 1000\n- Meer dan 5000\n- Meer dan 6800',
                'Hoeveel verschillende tijdzones heeft China?\n- 1\n- 2\n- 5',
                'Waar staat het hoogste gebouw in Azie\n- India\n- Japan\n- Taiwan',
                'Hoeveel tuk tuks rijden er in Bangkok, Thailand?\n- Ongeveer 2000\n- Ongeveer 10000\n- Ongeveer 20000',
                'Waar komt thee oorspronkelijk vandaan?\n- China\n- Indonesie\n- Sri Lanka',
                'Hoe lang is de Chinese muur?\n- 21 kilometer\n- 5 kilometer\n- 153 kilometer',
                'Wat is het rijkste land van Azie?\n- Japan\n- Singapore\n- Qatar',
                'Hoeveel procent van de wereldbevolking woont in Azie?\n- 60%\n- 30%\n- 40%']
    AZAnswers = ['China',
                'Met hun rechterhand',
                'Meer dan 6800',
                '1',
                'India',
                'Ongeveer 10000',
                'Sri Lanka',
                '21 kilometer',
                'Qatar',
                '60%']
    AFQuestions = ['Wat is de grootste zandwoestijn ter wereld?\n- Sahara\n- Kalahari\n- Grote Arabische Woestijn',
                'Welk land in afrika heeft het grootste inwonersaantal?\n- Egypte\n- Nigeria\n- Zuid-Afrika',
                'Welk dier uit afrika is naar een rivier genoemd?\n- Nijlpaard\n- Amazone kikker\n- Niger Slang',
                'Welk land in afrika staat bekend om een bepaald dier?\n- Egypte voor nijlpaarden\n- Madagascar voor ringstaartmaki’s\n- Algerije voor leeuwen',
                'Wat is de grootste piramide in Afrika?\n- Gizeh\n- Cheops\n- Khafre',
                'In welk land in Afrika komen geen krokodillen voor?\n- Marokko\n- Nigeria\n- Centraal Afrikaanse Republiek',
                'Wat is de hoogst gemeten temperatuur in de sahara ooit gemeten?\n- 63,2\n- 59,2\n- 57,7',
                'Wat is de hoofdstad van Zuid-Afrika?\n- Kaapstad\n- Johannesburg\n- Alexandrie']
    AFAnswers = ['Sahara',
                'Nigeria',
                'Nijlpaard',
                'Madagascar voor ringstaartmaki’s',
                'Cheops',
                'Marokko',
                '57,7',
                'Kaapstad']
    OAQuestions = ['Wat is het grootste reptiel ter wereld?\n- Komodovaraan\n- Zoutwaterkrokodil\n- Python',
                'Wat is de hoofdstad van Australie?\n- Sydney\n- Melbourne\n- Canberra',
                'Hoeveel van de 15 giftigste slangen komen voor in Australie?\n- 5 van de 15\n- 10 van de 15\n- 15 van de 15',
                'Welk dier komt van nature alleen in Australie voor?\n- Koala\n- Kangoeroe\n- Kameel',
                'Welk dier leeft niet op Antarctica?\n- Pinguin\n- IJsbeer \n- Zeehonden',
                'Staan er vulkanen op Antarctica?\n- Ja\n- Nee',
                'Door hoeveel oceanen wordt Antarctica omringd?\n- 1\n- 2\n- 3',
                'Welke van de volgende fruitsoorten is ook een vogelsoort?\n- Mango\n- Kiwi\n- Papaya',
                'Welk beroemd gebouw komt in Australie voor?\n- De Eiffeltoren\n- De Grand Canyon\n- Het Operagebouw',
                'Uit wat voor soort water bestaat het ijs op Antarctica?\n- Zoet water\n- Zout water']
    OAAnswers = ['Zoutwaterkrokodil',
                'Canberra',
                '10 van de 15',
                'Koala',
                'Pinguin',
                'Ja',
                '3',
                'Kiwi',
                'Het Operagebouw',
                'Zoet water']
def draw():
    # Globals voor spelers
    global speler1, speler2, speler3, speler4, punten1, punten2, punten3, punten4

    # Globals voor vraag kaart buttons
    global vraagButton, vraagButtonClicked, vraagButtonBack

    # Globals voor pech kaart buttons
    global pechKaartButton, pechKaartButtonClicked, pechKaartButtonBack

    # Globals voor dobbelsteen buttons
    global diceButton, diceButtonClicked, diceButtonBack

    # Globals voor Noord-Amerika
    global NAButton, NAButtonClicked, NAQuestions, NAAnswers

    # Globals voor Zuid-Amerika
    global SAButton, SAButtonClicked, SAQuestions, SAAnswers

    # Globals voor Oceanië/Antarctica
    global OAButton, OAButtonClicked, OAQuestions, OAAnswers

    # Globals voor Azië
    global AZButton, AZButtonClicked, AZQuestions, AZAnswers

    # Globals voor Afrika
    global AFButton, AFButtonClicked, AFQuestions, AFAnswers

    # Globals voor Europa
    global EUButton, EUButtonClicked, EUQuestions, EUAnswers

    # Globals voor overige buttons
    global startButton, startButtonClicked, quitFromGameButton, quitFromMenuButton, showAnswerButton

    # Overige globals
    global cp5, randPechkaart, side, pechIndex, buttonwidthCont, buttonheightCont

    # Globals voor fonts
    global normalTextFont, titleFont, continentButtonFont

    background(unhex("FFFFFF"))
    textFont(titleFont)
    text(str("De Grote Wereld Quiz"), width / 2 - 400 , 120)
    vraagButton.setVisible(False)
    diceButton.setVisible(False)
    pechKaartButton.setVisible(False)
    quitFromGameButton.setVisible(False)
    diceButtonBack.setVisible(False)
    vraagButtonBack.setVisible(False)
    pechKaartButtonBack.setVisible(False)
    NAButton.setVisible(False)
    SAButton.setVisible(False)
    EUButton.setVisible(False)
    AZButton.setVisible(False)
    AFButton.setVisible(False)
    OAButton.setVisible(False)
    showAnswerButton.setVisible(False)
    quitFromMenuButton.setVisible(True)

    if startButtonClicked == True:
        background(unhex("FFFFFF"))
        fill(0)
        textFont(normalTextFont)
        fill(240)
        rect(250, 150, 200, 60) #speler 1
        rect(250, 220, 200, 60) #speler 2
        rect(250, 290, 200, 60) #speler 3
        rect(250, 360, 200, 60) #speler 4
        fill(0)
        textFont(titleFont)
        text(str("Scorebord"), width / 2 - 190 , 90)
        textFont(normalTextFont)
        text(str("speler1"), 270, 190)
        text(str("Punten:"), 570, 190)
        text(str(punten1), 695, 190)
        text(str("speler2"), 270, 260)
        text(str("Punten:"), 570, 260)
        text(str(punten2), 695, 260)
        text(str("speler3"), 270, 330)
        text(str("Punten:"), 570, 330)
        text(str(punten3), 695, 330)
        text(str("speler4"), 270, 400)
        text(str("Punten:"), 570, 400)
        text(str(punten4), 695, 400)
        # + buttons in volgorde
        fill(200)
        rect(740, 160, 45, 45, 7)
        rect(740, 230, 45, 45, 7)
        rect(740, 300, 45, 45, 7)
        rect(740, 370, 45, 45, 7)
        # - buttons in volgorde
        rect(800, 160, 45, 45, 7)
        rect(800, 230, 45, 45, 7)
        rect(800, 300, 45, 45, 7)
        rect(800, 370, 45, 45, 7)
        fill(0)
        text(str("+"), 754, 193)
        text(str("+"), 754, 263)
        text(str("+"), 754, 333)
        text(str("+"), 754, 403)
        text(str("-"), 817, 191)
        text(str("-"), 817, 261)
        text(str("-"), 817, 331)
        text(str("-"), 817, 401)
        if diceButtonClicked == True:
            # Dobbelsteen scherm
            background(unhex("FFFFFF"))
            vraagButton.setVisible(False)
            diceButton.setVisible(False)
            pechKaartButton.setVisible(False)
            quitFromGameButton.setVisible(False)
            diceButtonBack.setVisible(True)
            vraagButtonBack.setVisible(False)
            pechKaartButtonBack.setVisible(False)
            NAButton.setVisible(False)
            SAButton.setVisible(False)
            EUButton.setVisible(False)
            AZButton.setVisible(False)
            AFButton.setVisible(False)
            OAButton.setVisible(False)
            showAnswerButton.setVisible(False)
            startButton.setVisible(False)
            quitFromMenuButton.setVisible(False)
            background(unhex("FFFFFF"))
            text(str(side), width / 2, height / 2)
        elif vraagButtonClicked == True:
            # Vraag scherm
            background(unhex("FFFFFF"))
            vraagButton.setVisible(False)
            diceButton.setVisible(False)
            pechKaartButton.setVisible(False)
            quitFromGameButton.setVisible(False)
            diceButtonBack.setVisible(False)
            vraagButtonBack.setVisible(True)
            pechKaartButtonBack.setVisible(False)
            NAButton.setVisible(True)
            SAButton.setVisible(True)
            EUButton.setVisible(True)
            AZButton.setVisible(True)
            AFButton.setVisible(True)
            OAButton.setVisible(True)
            showAnswerButton.setVisible(True)
            startButton.setVisible(False)
            quitFromMenuButton.setVisible(False)
            text(str("Kies een continent:"), 75, 50)
            text(str("Vragen kaart:"), width/2 + 210, 90)
            fill(unhex("FFFFF"))
            rect(850, 120, 330, 450, 10)
            if NAButtonClicked == True:
                fill(0)
                text(NAQuestions[randNA], 850, 120, 330, 450)
                SAButtonClicked = False
                EUButtonClicked = False
                AZButtonClicked = False
                AFButtonClicked = False
                OAButtonClicked = False
            if showAnswerNA == True:
                NAButtonClicked = False
                SAButtonClicked = False
                EUButtonClicked = False
                AZButtonClicked = False
                AFButtonClicked = False
                OAButtonClicked = False
                fill(0)
                text(NAAnswers[randNA], 850, 120, 330, 450)
            if SAButtonClicked == True:
                fill(0)
                text(SAQuestions[randSA], 850, 120, 330, 450)
                NAButtonClicked = False
                EUButtonClicked = False
                AZButtonClicked = False
                AFButtonClicked = False
                OAButtonClicked = False
            if showAnswerSA == True:
                SAButtonClicked = False
                NAButtonClicked = False
                EUButtonClicked = False
                AZButtonClicked = False
                AFButtonClicked = False
                OAButtonClicked = False
                fill(0)
                text(SAAnswers[randSA], 850, 120, 330, 450)
            if EUButtonClicked == True:
                fill(0)
                text(EUQuestions[randEU], 850, 120, 330, 450)
                NAButtonClicked = False
                SAButtonClicked = False
                AZButtonClicked = False
                AFButtonClicked = False
                OAButtonClicked = False
            if showAnswerEU == True:
                SAButtonClicked = False
                NAButtonClicked = False
                EUButtonClicked = False
                AZButtonClicked = False
                AFButtonClicked = False
                OAButtonClicked = False
                fill(0)
                text(EUAnswers[randEU], 850, 120, 330, 450)
            if AZButtonClicked == True:
                fill(0)
                text(AZQuestions[randAZ], 850, 120, 330, 450)
                NAButtonClicked = False
                SAButtonClicked = False
                EUButtonClicked = False
                AFButtonClicked = False
                OAButtonClicked = False
            if showAnswerAZ == True:
                SAButtonClicked = False
                NAButtonClicked = False
                EUButtonClicked = False
                AZButtonClicked = False
                AFButtonClicked = False
                OAButtonClicked = False
                fill(0)
                text(AZAnswers[randAZ], 850, 120, 330, 450)
            if AFButtonClicked == True:
                fill(0)
                text(AFQuestions[randAF], 850, 120, 330, 450)
                NAButtonClicked = False
                SAButtonClicked = False
                EUButtonClicked = False
                AZButtonClicked = False
                OAButtonClicked = False
            if showAnswerAF == True:
                SAButtonClicked = False
                NAButtonClicked = False
                EUButtonClicked = False
                AZButtonClicked = False
                AFButtonClicked = False
                OAButtonClicked = False
                fill(0)
                text(AFAnswers[randAF], 850, 120, 330, 450)
            if OAButtonClicked == True:
                fill(0)
                text(OAQuestions[randOA], 850, 120, 330, 450)
                NAButtonClicked = False
                SAButtonClicked = False
                EUButtonClicked = False
                AZButtonClicked = False
                AFButtonClicked = False
            if showAnswerOA == True:
                SAButtonClicked = False
                NAButtonClicked = False
                EUButtonClicked = False
                AZButtonClicked = False
                AFButtonClicked = False
                OAButtonClicked = False
                fill(0)
                text(OAAnswers[randOA], 850, 120, 330, 450)

        elif pechKaartButtonClicked == True:
            # Pech kaart screen
            background(unhex("FFFFFF"))
            vraagButton.setVisible(False)
            diceButton.setVisible(False)
            pechKaartButton.setVisible(False)
            quitFromGameButton.setVisible(False)
            diceButtonBack.setVisible(False)
            vraagButtonBack.setVisible(False)
            pechKaartButtonBack.setVisible(True)
            NAButton.setVisible(False)
            SAButton.setVisible(False)
            EUButton.setVisible(False)
            AZButton.setVisible(False)
            AFButton.setVisible(False)
            OAButton.setVisible(False)
            showAnswerButton.setVisible(False)
            startButton.setVisible(False)
            quitFromMenuButton.setVisible(False)
            text(pechIndex[randPechkaart], 510, height / 2 - 60, 300, 450)
            text(str("Pech kaart"), width/2 - 95, 90)
            fill(unhex("FFFFF"))
            rect(490, 120, 330, 450, 10)

        else:
            # Spel
            vraagButton.setVisible(True)
            diceButton.setVisible(True)
            pechKaartButton.setVisible(True)
            quitFromGameButton.setVisible(True)
            diceButtonBack.setVisible(False)
            vraagButtonBack.setVisible(False)
            pechKaartButtonBack.setVisible(False)
            NAButton.setVisible(False)
            SAButton.setVisible(False)
            EUButton.setVisible(False)
            AZButton.setVisible(False)
            AFButton.setVisible(False)
            OAButton.setVisible(False)
            showAnswerButton.setVisible(False)
            startButton.setVisible(False)
            quitFromMenuButton.setVisible(False)
            if mousePressed:
                # Spel afsluiten func.
                if isMouseWithinSpace(455, 500, 350, 125):
                    DiceButtonPressed = False
                if isMouseWithinSpace(1050, 30, 200, 70):
                    exit()
        if punten1 == 10 or punten2 == 10 or punten3 == 10 or punten4 == 10:
            #winnaarsscherm
            background(unhex("FFFFFF"))
            vraagButton.setVisible(False)
            diceButton.setVisible(False)
            pechKaartButton.setVisible(False)
            quitFromGameButton.setVisible(True)
            diceButtonBack.setVisible(False)
            vraagButtonBack.setVisible(False)
            pechKaartButtonBack.setVisible(False)
            NAButton.setVisible(False)
            SAButton.setVisible(False)
            EUButton.setVisible(False)
            AZButton.setVisible(False)
            AFButton.setVisible(False)
            showAnswerButton.setVisible(False)
            startButton.setVisible(False)
            quitFromMenuButton.setVisible(False)
            OAButton.setVisible(False)
            if punten1 == 10:
                text("Speler 1 heeft gewonnen!", width / 2 - 150, height / 2)
            elif punten2 == 10:
                text("Speler 2 heeft gewonnen!", width / 2 - 150, height / 2)
            elif punten3 == 10:
                text("Speler 3 heeft gewonnen!", width / 2 - 150, height / 2)
            elif punten4 == 10:
                text("Speler 4 heeft gewonnen!", width / 2 - 150, height / 2)
def isMouseWithinSpace(x,y,w,h):
    # MouseClick function
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False

def mousePressed():
    # Globals voor spelers
    global speler1, speler2, speler3, speler4, punten1, punten2, punten3, punten4

    # Globals voor vraag kaart buttons
    global vraagButton, vraagButtonClicked, vraagButtonBack

    # Globals voor pech kaart buttons
    global pechKaartButton, pechKaartButtonClicked, pechKaartButtonBack

    # Globals voor dobbelsteen buttons
    global diceButton, diceButtonClicked, diceButtonBack

    # Globals voor Noord-Amerika
    global NAButton, NAButtonClicked, NAQuestions, NAAnswers

    # Globals voor Zuid-Amerika
    global SAButton, SAButtonClicked, SAQuestions, SAAnswers

    # Globals voor Oceanië/Antarctica
    global OAButton, OAButtonClicked, OAQuestions, OAAnswers

    # Globals voor Azië
    global AZButton, AZButtonClicked, AZQuestions, AZAnswers

    # Globals voor Afrika
    global AFButton, AFButtonClicked, AFQuestions, AFAnswers

    # Globals voor Europa
    global EUButton, EUButtonClicked, EUQuestions, EUAnswers

    # Globals voor overige buttons
    global startButton, startButtonClicked, quitFromGameButton, quitFromMenuButton, showAnswerButton

    # Overige globals
    global cp5, randPechkaart, side, pechIndex, buttonwidthCont, buttonheightCont

    # Globals voor fonts
    global normalTextFont, titleFont, continentButtonFont

    # De + buttons punten erbij
    if diceButtonClicked == False and vraagButtonClicked == False and pechKaartButtonClicked == False :
        if punten1 < 10 and punten2 < 10 and punten3 < 10 and punten4 < 10:
            if isMouseWithinSpace(740, 160, 45, 45):
                punten1 = punten1 + 1
            elif isMouseWithinSpace(740, 230, 45, 45):
                punten2 = punten2 + 1
            elif isMouseWithinSpace(740, 300, 45, 45):
                punten3 = punten3 + 1
            elif isMouseWithinSpace(740, 370, 45, 45):
                punten4 = punten4 + 1
            # De - buttons punten er af
            elif isMouseWithinSpace(800, 160, 45, 45):
                punten1 = punten1 - 1
                if punten1 < 0:
                    punten1 = 0
            elif isMouseWithinSpace(800, 230, 45, 45):
                punten2 = punten2 - 1
                if punten2 < 0:
                    punten2 = 0
            elif isMouseWithinSpace(800, 300, 45, 45):
                punten3 = punten3 - 1
                if punten3 < 0:
                    punten3 = 0
            elif isMouseWithinSpace(800, 370, 45, 45):
                punten4 = punten4 - 1
                if punten4 < 0:
                    punten4 = 0
    global diceButtonClicked, side, vraagButtonClicked, pechKaartButtonClicked, NAButtonClicked, startButtonClicked
    if startButtonClicked == False:
        if isMouseWithinSpace(455, 300, 350, 125):
            startButtonClicked = True
        if isMouseWithinSpace(455, 450, 350, 125):
            exit()
    if isMouseWithinSpace(455, 500, 350, 125) and not vraagButtonClicked and not pechKaartButtonClicked:
        if diceButtonClicked == True:
            side = int(random(1, 7))
        diceButtonClicked = not diceButtonClicked
    if isMouseWithinSpace(75, 500, 350, 125):
        vraagButtonClicked = not vraagButtonClicked
    if vraagButtonClicked:
        showAnswerNA = False
        showAnswerSA = False
        showAnswerEU = False
        showAnswerAZ = False
        showAnswerAF = False
        showAnswerOA = False
        # NA
        if isMouseWithinSpace(75, 80, buttonwidthCont, buttonheightCont):
            randNA = int(random(14))
            NAButtonClicked = not NAButtonClicked
        if isMouseWithinSpace(850, 600, 330, 60) and NAButtonClicked == True:
            showAnswerNA = not showAnswerNA
        # SA
        if isMouseWithinSpace(75, 150, buttonwidthCont, buttonheightCont):
            randSA = int(random(7))
            SAButtonClicked = not SAButtonClicked
        if isMouseWithinSpace(850, 600, 330, 60) and SAButtonClicked == True:
            showAnswerSA = not showAnswerSA
        # EU
        if isMouseWithinSpace(75, 220, buttonwidthCont, buttonheightCont):
            randEU = int(random(16))
            EUButtonClicked = not EUButtonClicked
        if isMouseWithinSpace(850, 600, 330, 60) and EUButtonClicked == True:
            showAnswerEU = not showAnswerEU
        # AZ
        if isMouseWithinSpace(75, 290, buttonwidthCont, buttonheightCont):
            randAZ = int(random(10))
            AZButtonClicked = not AZButtonClicked
        if isMouseWithinSpace(850, 600, 330, 60) and AZButtonClicked == True:
            showAnswerAZ = not showAnswerAZ
        # AF
        if isMouseWithinSpace(75, 360, buttonwidthCont, buttonheightCont):
            randAF = int(random(8))
            AFButtonClicked = not AFButtonClicked
        if isMouseWithinSpace(850, 600, 330, 60) and AFButtonClicked == True:
            showAnswerAF = not showAnswerAF
        # OA
        if isMouseWithinSpace(75, 430, buttonwidthCont, buttonheightCont):
            randOA = int(random(10))
            OAButtonClicked = not OAButtonClicked
        if isMouseWithinSpace(850, 600, 330, 60) and OAButtonClicked == True:
            showAnswerOA = not showAnswerOA

    if isMouseWithinSpace(835, 500, 350, 125):
        randPechkaart = int(random(6))
        pechKaartButtonClicked = not pechKaartButtonClicked
    else:
        pass
