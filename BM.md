# Bepaling van de constante van Boltzmann

```{iframe} https://www.youtube.com/embed/oL4-ipL62pQ?si=KD-1YDAk-Nvbc5Sm
```

## Doel 
### Practicumdoel
In dit practicum ga je het $(I,V)$-karakteristiek van een silicium diode bepalen waarbij je metingen doet aan hele kleine stroomsterktes.
Je mag zelf bepalen of je de Boltzmann constante bepaalt, of de idealiteitsfactor van de diode.

### Leerdoel
Hoewel moderne DMM's behoorlijk ideale meetinstrumenten zijn, moeten we bij metingen in een schakeling rekening houden met de mogelijkheid dat de meter de spanningen en stromen in de schakeling verstoort.
Het doel van deze proef is leren omgaan met de Digitale Multimeters (DMM's).
Daarnaast leer je werken met spanningsdeler en bouw je een eenvoudig elektrische schakeling.

## Voorbereiding ($t$=2h)

### De constante van Boltzmann en de diode karakteristiek
De constante van Boltzmann is de evenredigheidsconstante die temperatuur en (thermische) energie aan elkaar koppelt volgens:

$$ E = k_{B} T $$

De constante van Boltzmann komt ook voor in de zogenaamde Boltzmann verdeling.
De Boltzmann verdeling geeft de waarschijnlijkheid van de energie van een elektron aan als functie van de temperatuur ($p_i \propto e^{-\frac{E_i}{kT}}$).
In een halfgeleider, zoals een diode, is de energie van de elektronen ook verdeeld volgens de Boltzmann verdeling, waarbij de gemiddelde energie van een elektron gelijk is aan $k_BT$ ($T$ is de absolute temperatuur en $k_B$ is de Boltzmann constante).

Bij een diode is er sprake van een (energie)barrière waardoor elektronen niet vrij kunnen bewegen.
De grootte van de elektrische stroom bij kleine spanningen over de diode hangt dan af van de hoogte van de barrière ten opzichte van de energie van de elektronen.
De hoogte van de barrière wordt mede bepaald door de grootte van de voorwaartse spanning.
Hoe hoger de voorwaartse spanning des te lager de barrière.
Om dit principe beter te snappen, kun je de achtergrond informatie over halfgeleiderdiodes lezen.
Deze stof is niet noodzakelijk voor de uitvoering van deze proef.

De Boltzmann verdeling van de energie van de elektronen en de aanwezigheid van een barrière wordt mooi tot uiting gebracht in een theoretische formule die het verband tussen de (voorwaartse) stroom door en spanning over een diode beschrijft.
Het verband tussen de stroom ($I_D$) door, en de spanning ($V_D$) over de diode wordt gegeven door de exponentiële functie:

$$ I_{D}\left(V_{D}\right)=I_{0}\left(e^{\frac{-q V_{D}}{n k_{B} T}}-1\right) $$(eq:stroom_diode)

$q$ is hier de lading van een elektron, $-1.602 \times 10^{-19}$ C, $k_B$ is de Boltzmann constante, $n$ is de idealiteitsfactor (hangt af van waar precies de recombinatie plaatsvindt; $n = 2.0 \pm 0.1$ voor Si) en $I_0$ is de sperstroom, de stroom die loopt als $V_D$ sterk negatief wordt.
Schematisch ziet de $(I,V)$ karakteristiek er op lineaire schaal uit als weergegeven in figuur {numref}`{number} <fig:ii1_fig_schematisch>`.

```{figure} Figures/BM/diodekarakteristiek.jpg
---
width: 80%
name: fig:ii1_fig_schematisch
---
Links: Diode karakteristiek (doorgetrokken lijn), vereenvoudigde diode karakteristiek (gestreepte lijn).
Rechts: het standaard symbool voor een diode met voorwaartse stroom.
Geheel rechts: Een donker randje op een diode geeft de aansluiting met het n-type gebied aan.
```

In figuur {numref}`{number} <fig:ii1_fig_schematisch>` zien we ook dat bij zekere negatieve spanning $V_b$ de stroom plotseling sterk toeneemt.
Dit noemen wij de breakdown spanning van de diode.
De diode gedraagt zich dan bijna als een kortsluiting.
Dit gedrag wordt niet beschreven door vergelijking {eq}`eq:stroom_diode`.
Wat er gebeurt, is dat de spanning over het gebied zonder vrije ladingsdragers zo groot wordt dat de elektronen van de atomen worden 'losgetrokken' en als er één gaat, gaan er meerdere (lawine effect).

Maken we een plot van vergelijking {eq}`eq:stroom_diode` waarbij we de $^{10}$log van $I_D$ uitzetten tegen $V_D$ dan vinden we de doorgetrokken kromme in figuur {numref}`{number} <fig:karakteristiek_halfgeleider>`.

```{figure} Figures/BM/VIkarakteristiek.jpg
---
width: 80%
name: fig:karakteristiek_halfgeleider
---
($I,V$)-karakteristiek van een halfgeleiderdiode op semi-log schaal.
De meetpunten volgen vgl. {eq}`eq:stroom_diode`.
De gestreepte lijn wordt verkregen door de "-1" in vgl. {eq}`eq:stroom_diode` weg te laten.
Grafiek mogelijk gemaakt d.m.v. dataset van eerstejaars studenten uit 2019.
```

We zien voor $V_D>0.1 $V een rechte lijn.
Dit wordt veroorzaakt door het volgende.
Voor het genoemde spanningsgebied is $e^{\frac{-q V_{D}}{n k_{B} T}}>>1$.
De stroom door de diode wordt in dat gebied dan ook goed beschreven met 

$$ I_{D}=I_{0} e^{\frac{-q V_{D}}{n k_{B} T}} $$ (eq:fitfunc)

Nemen we nu links en rechts de logaritme van deze vergelijking dan wordt dit

$$ \log_{10}(I_D)=\log_{10}(I_0)+\log_{10}(e)\frac{-q}{nk_BT}V_d $$

Dit is gelijk aan een vergelijking van een rechte lijn $y=cx+d$.
Deze vergelijking kun je gebruiken om de constante van Boltzmann te bepalen op basis van een handgemaakte grafiek.
Echter, met de rekenkracht van de huidige computers is er geen goede reden te bedenken waarom te functie fitten op basis van het gehele domein, en dus op basis van vergelijking {eq}`eq:stroom_diode`.

```{tip}
:class: dropdown
De afsnijding met de y-as geeft $d$ en dus $I_0$.
Deze waarde kan handmatig bepaald worden en als initiële schatting (`p0`) in Python meegegeven worden.
```

Willen we de Boltzmann verdeling nader bestuderen, of een eigenschap (bijvoorbeeld de idealiteitsfactor) van de diode bepalen, dan is het dus de bedoeling dat we de sterkte van de stroom als functie van de spanning over de diode bepalen.
Zowel het meten van een stroom als het meten van een spanning kan met een digitale multimeter (DMM).

### Metingen met DMM's
Digitale multimeters zijn veelzijdige meetinstrumenten die onder meer gebruikt worden voor het meten van spanning, stroom en weerstand.
Bij geavanceerdere modellen kun je de DMM met een computer besturen en uitlezen en frequenties, tijdsintervallen, capaciteiten, inducties, continuïteit, temperatuur, diode info etc. meten.

In deze proef beperken we ons tot gelijkspannings-, gelijkstroom- en weerstandsmetingen.
Het is van belang je te realiseren dat het hart van een DMM wordt gevormd door een Analog Digital Convertor (ADC).
Deze eenheid zet een getal op zijn display dat evenredig is met de spanning die op de ingang wordt aangeboden.
Het bereik waarbinnen de ADC werkt, is meestal gelijk aan het gevoeligste bereik van de DMM voor gelijkspanningsmetingen (b.v. $-100 \; \mathrm{mV}$ tot $+100 \; \mathrm{mV}$).
 Als we de meter op een minder gevoelig meetbereik zetten, schakelen we verzwakkers in die de ingangspanning reduceren tot in het bereik van de ADC.
 Dit is schematisch in Figuur ({numref}`{number} <fig:DMM>`) links weergeven.
 Om spanning met een DMM te meten gebruiken we de ingangen **V** en **com** of **hi** en **lo**.

Als wij een gelijkstroommeting uitvoeren, gebruiken wij de ingangen **I** of **mA** of **A** en **com** of **lo**.
We meten bij een gelijkstroommeting in feite de gelijkspanning over een weerstand $R_s$ (zie figuur {numref}`{number} <fig:DMM>` links onder).
$R_s$ wordt de shunt weerstand genoemd omdat daar de stroom doorheen loopt en niet door de rest van de meter.
Deze weerstand kunnen we beschouwen als de inwendige weerstand van de stroommeter.
In de *laagste* stroombereiken is $R_s$ van de orde $100 \; \Omega$ tot $1000 \; \Omega$.

```{figure} Figures/BM/weerstandsmeting.jpg
---
width: 80%
name: fig:DMM
---
Principe van gelijkspanning, gelijkstroom en weerstandsmeting met een DMM.
```

Als we met de DMM weerstandswaarden meten, wordt er met behulp van een interne stroombron een stroom door de weerstand gestuurd en wordt de spanning over de weerstand gemeten (figuur {numref}`{number} <fig:DMM>` rechts).
De grootte van de meetstroom wordt opgegeven in de handleiding van de DMM.
Voor de laagste weerstands-bereiken is bijvoorbeeld $1 \; \mathrm{mA}$ een typische waarde.

```{note}
:class: dropdown
De schema's in figuur {numref}`{number} <fig:DMM>` zijn min of meer equivalente schema's.
Met name voor weerstandsmetingen bestaan veel variaties.
```

Bij het aansluiten van DMM's moeten we ons ervan bewust zijn dat, zoals in figuur {numref}`{number} <fig:DMM>` links al is aangegeven, voor stroommeting heel vaak een andere ingang wordt gebruikt dan voor spannings- en weerstandsmetingen.
In figuur {numref}`{number} <fig:aansluitingen>` zijn de ingangen van een aantal DMM's zoals wij die op het practicum gebruiken weergeven.
Links de Dynatek D9100, $3\frac{1}{2}$ digit DMM, in het midden de $5\frac{1}{2}$ digit Thurlby 1905a en rechts de $6\frac{1}{2}$ digit Agilent 34401A.

```{figure} Figures/BM/DMMpoorten.jpg
---
width: 80%
name: fig:aansluitingen
---
Aansluitingen voor (van links naar rechts) de Dynatek, Thurlby en Agilent DMM.
```

```{warning} 
De kans is zeer groot dat, als wij van stroommeting overgaan op spanningsmeting (van b.v. een voedingsbron) en vergeten de draad uit de I-ingang naar de V-ingang te verplaatsen, op z'n minst de zekering voor de weerstand $R_s$ (zie figuur {numref}`{number} <fig:DMM>` links) wordt opgeblazen.
Let hier op!
```

(subsubsec:nauwkeurigheidsspecificaties)= 
### Nauwkeurigheidspecificaties van een digitale meter

We zouden kunnen veronderstellen dat de nauwkeurigheid van een meter bepaald wordt door een tel van de laatste decimaal van de uitlezing.
Zo simpel is het meestal niet.
Een fabrikant geeft de nauwkeurigheid van een DMM meestal op in $\pm$(..\% aflezing + ..\% bereik) of zelfs $\pm$(..\% aflezing + ..\% bereik + ..tellen (counts, digits)).
Deze manier om de nauwkeurigheid op te geven is redelijk als we bedenken dat het verband tussen de ingangsspanning en wat er op de uitlezing staat in hoge mate lineair is ($V_{\text{uit}} = aV_{\text{in}} + b$).
Fouten in $V_{\text{uit}}$ kunnen dan goed gespecificeerd worden door fouten in $a$ en $b$ op te geven.
De specificatie +\% aflezing correspondeert met de nauwkeurigheid van de "gain" (= versterking) $a$ en de aanduiding +\% bereik + .. tellen correspondeert met de "offset" (= afsnijding) $b$, die in het ideale geval precies nul is (zie figuur {numref}`{number} <fig:nauwkeurigheid_DMM>`).

```{figure} Figures/BM/DMMmeting.png
---
width: 80%
name: fig:nauwkeurigheid_DMM
---
De nauwkeurigheid van een DMM wordt opgegeven door de nauwkeurigheid van de helling (gain) en de afsnijding (offset) van het (veronderstelde) lineaire verband tussen de ingangsspanning en de waarde op het display op te geven.
```

```{admonition} Voorbeeld
:class: dropdown
Stel we lezen af: $1.234 \; \mathrm{V}$ op de $3\frac{1}{2}$ cijfer DMM.
Hieruit mag je dus niet zomaar afleiden dat de nauwkeurigheid van de meting beter dan $1 \; \mathrm{mV}$ is.
Voor de Dynatek D9100 wordt voor het 2 V bereik opgegeven: $\pm(0.5\%$ van de aflezing + $1 \; \mathrm{tel})$.
Dus: $0.5\%$ van de aflezing is $6 \; \mathrm{mV}$.
Plus $1 \; \mathrm{mV}$ van het digit geeft dus een nauwkeurigheid van $7 \; \mathrm{mV}$.
Het resultaat van de meting is $1.234 \pm 0.007 \; \mathrm{V}$.
Nauwkeurigheid wordt ook vaak opgegeven in ppm (parts per million, $1\% = 10000 \; \mathrm{ppm}$).
```

De resolutie van een digitaal instrument is de verhouding van het kleinste aantal tellen tot het grootste aantal tellen dat op het display kan worden weergegeven.
it wordt in feite bepaald door het aantal tellen (counts) dat kan worden weergegeven en dat aantal hangt natuurlijk af van het aantal cijfers.
Een simpele DMM heeft vaak $3\frac{1}{2}$ cijfers.
Dit betekent 3 hele cijfers (elk met waarden van 0 tot en met 9) plus een half cijfer dat de waarden 0 of $\pm1$ kan aannemen.
Dus een $3\frac{1}{2}$ cijfer display kan 0 tot 1999 weergeven, totaal 2000 tellen.
De resolutie van die DMM is $1/2000$ of wel $0.05\%$.

De gevoeligheid bij een meting is de kleinste verandering van het te meten signaal die kan worden waargenomen.
Een gevoeligheid bij een meting van $1 \; \mathrm{\mu V}$ impliceert dat veranderingen in het signaal kleiner dan $1 \; \mathrm{\mu V}$  niet kunnen worden waargenomen.
De gevoeligheid hangt mede af van de grootte van het signaal dat we willen meten.
Immers, de grootte van het signaal bepaalt het gevoeligste meetbereik waarop gemeten kan worden.

```{admonition} Voorbeeld
:class: dropdown
Stel we willen een spanning van ongeveer 15 V meten met een 3$\frac{1}{2}$ cijfer DMM.
Het gevoeligste bereik waarop we deze spanning kunnen meten, is het $20 \; \mathrm{V}$ bereik.
De kleinste verandering van het signaal die kan worden waargenomen is dan $10 \; \mathrm{mV}$ (ga na).
Voor een 5$\frac{1}{2}$ cijfer DMM is dit $0.1 \; \mathrm{mV}$.
Met een 3$\frac{1}{2}$ cijfer DMM kun je ook een gevoeligheid van $0.1 \; \mathrm{mV}$  halen, maar dan alleen voor signalen kleiner dan $200 \; \mathrm{mV}$.
De ultieme gevoeligheid van een meetinstrument hangt af van zijn resolutie en het laagste meetbereik.
Bijvoorbeeld de gevoeligheid van een 6$\frac{1}{2}$ cijfer DMM met een laagste meetbereik van $200 \; \mathrm{mV}$ is $0.1 \; \mathrm{\mu V}$.
```

(subsec:gebruik_dmm)=
### Gebruik van DMM's in een schakeling; ideale en niet-ideale spannings- en stroommeters

Bij metingen in een schakeling is het van belang dat de DMM de stromen en de spanningen in de schakeling niet beïnvloedt.
Het zal van de meter en de schakeling afhangen of er wel of niet significante beïnvloeding plaatsvindt.
Om dit probleem op een systematische manier aan te pakken is het zinvol het concept van ideale spannings- en stroommeters te introduceren.
Het spreekt vanzelf dat we een meter ideaal noemen als het plaatsen van de meter in een schakeling geen enkele invloed heeft op de eigenschappen (spanningen en stroomsterktes) van het circuit.

Bij het meten van de spanning tussen twee punten wordt de meter parallel gezet met een deel van de schakeling.
Loopt er door de meter geen stroom, dan worden de stromen (en daarmee de spanningen) in de schakeling niet beïnvloed door de meter.
Een ideale spanningsmeter is dus een meter waardoor geen stroom loopt.
Wij kunnen ook zeggen: een ideale spanningsmeter heeft een oneindig hoge weerstand (zie figuur {numref}`{number} <fig:ideaal_niet_ideaal>` meest links).

Door een niet-ideale spanningsmeter loopt dus wel stroom, de weerstand tussen de twee aansluitpunten is niet oneindig.
Een niet-ideale spanningsmeter kunnen we representeren door een parallelschakeling van een ideale spanningsmeter en een weerstand (zie figuur {numref}`{number} <fig:ideaal_niet_ideaal>` tweede figuur van links).

```{figure} Figures/BM/VAmeters.jpg
---
width: 80%
name: fig:ideaal_niet_ideaal
---
Representatie van een ideale en niet-ideale spanningsmeter (links) en een ideale en niet-ideale stroommeter (rechts).
```

Bij een stroommeting wordt de meter in een bestaande tak van de schakeling in serie met de al aanwezige elementen opgenomen.
Valt er over de meter geen spanning dan worden de spanningen (en daarmee de stromen) in de schakeling niet beïnvloed door de meter.
Een ideale stroommeter is dus een meter waarover geen spanning valt.
Wij kunnen ook zeggen: de weerstand van een ideale stroommeter is gelijk aan nul (zie figuur {numref}`{number} <fig:ideaal_niet_ideaal>` tweede figuur van rechts).

Over een niet-ideale stroommeter valt dus wel spanning en zijn weerstand is niet gelijk aan nul.
Een niet-ideale stroommeter kan gerepresenteerd worden door serieschakeling van een ideale stroommeter en een weerstand (zie figuur {numref}`{number} <fig:ideaal_niet_ideaal>` uiterst rechts).

De schema's die het niet-ideale gedrag van de meters representeren zijn handig als we willen weten of de verstoring door de meters belangrijk is of niet.
We zien bijvoorbeeld direct dat het meten van de spanning over een weerstand die in grootte vergelijkbaar is met de weerstand van de meter ($R_{\text{i}}$), tot verstoringen van de oorspronkelijke stroom/spanningsverdeling leidt.
Zo zal een stroommeter verstorend werken als zijn weerstand ($R_{\text{i}}$) niet te verwaarlozen is ten opzichte van de andere weerstanden in de tak waarin de meter is opgenomen.

```{admonition} Voorbeeld
:class: dropdown
De spanning over een weerstand van $100 \; \mathrm{k\Omega}$ wordt gemeten met een DMM met een weerstand van $1.0 \; \mathrm{M\Omega}$.
Beinvloedt de meting de eigenschappen van het oorspronkelijk circuit significant?

De DMM staat parallel aan de Ohmse weerstand.
De vervangingsweerstand is gelijk aan: $R_v = \frac{R_{DMM} \cdot R_O}{R_{DMM} + R_O}$ (ga zelf na!).
De vervangingsweerstand is dus $91 \; \mathrm{k\Omega}$! Dat is inderdaad een significant verschil.
```

De verstoring door het aanbrengen van de DMM in een ingewikkelde, onoverzichtelijke  situatie kan systematisch in beeld worden gebracht door de niet-ideale representatie van een spannings - of stroommeter in de schakeling te tekenen en de waarden van $R_{\text{i}}$ in de handleiding van de DMM op te zoeken.

Moderne digitale multimeters hebben op het spanningsmeetbereik een zeer hoge interne weerstand (b.v. $R_\text{i}=10 M\Omega$ of hoger).
Bij stroommeting zijn deze meters in de lage bereiken iets minder ideaal (b.v. $R_{\text{i}} = 1 k\Omega$).
Voor stroommeting wordt in de specificaties van een DMM $R_{\text{i}}$ vaak niet direct opgegeven.
Men specificeert de Voltage Burden: de maximale spanning die over de meter valt bij stroommeting.
De weerstand van de stroommeter wordt dan vaak gegeven door (Voltage Burden) / (meetbereik).

```{tip}
:class: dropdown
Met behulp van de wet van Ohm kunnen we natuurlijk ipv de stroom gewoon de spanning meten over een Ohmse weerstand met bekende weerstandswaarde.
Voorwaarde is natuurlijk dat die weerstand zelf de eigenschappen niet te veel verstoort.
```

```{exercise} 
:class: dropdown
* Voor de nauwkeurigheid van een DMM wordt voor het $10 \; \mathrm{V}$ bereik opgegeven: $0.0015\%$ van de aflezing en $0.0004\%$ van het bereik. 
De spanning die wordt afgelezen is $5.00000 \; \mathrm{V}$.
Wat is de nauwkeurigheid van de meting?
* Wat is de gevoeligheid bij het meten van een gelijkspanning van ongeveer $9 \; \mathrm{mV}$ met een 4$\frac{1}{2}$ digit DMM op het $200 \; \mathrm{mV}$ bereik?
```

```{exercise}
:class: dropdown
* Bekijk figuur {numref}`{number} <fig:karakteristiek_halfgeleider>`.
Leg uit waarom het direct meten van een stroomsterkte door de diode niet handig is.
* Leg ook uit waarom het direct meten van de spanning over de diode niet nauwkeurig is.
Denk aan het niet ideaal zijn van de meters.
```

(subsec:spanningsdeleropst)=
### Spanningsdeler
Om rekening te houden met het niet ideaal zijn van de meters, maken we in dit experiment gebruik van een spanningsdeler.
In zijn eenvoudigste vorm is een spanningsdeler niets anders dan een serieschakeling van twee weerstanden.
De (bron)spanning wordt dan gedeeld door de verschillende componenten in de schakeling.
De vergelijkingen voor de stroomsterkte en de spanning staan als geheugensteuntje weergegeven in par. {numref}`{number} <subsec:geheugensteun>` van de achtergrondinformatie.
Omdat de kennis van de spanningsdeler stof is wat in 4 VWO behandeld wordt, beschouwen we dit als voorkennis en wordt de benodigde kennis hieronder alleen getoetst.

```{exercise} 
:class: dropdown
Stel we hebben een spanningsdeler bestaande uit een $330 \; \Omega$ en een $1000 \; \Omega$ weerstand.
De maximale dissipatie in de weerstanden is $1 \; \mathrm{Watt}$.
* Hoeveel stroom mag er door de $330 \; \Omega$ en door de $1000 \; \Omega$ weerstanden maximaal lopen?
* Wij schakelen de weerstanden in serie. Hoeveel spanning mag erover de serieschakeling gezet worden zodat de maximaal toelaatbare dissipatie niet wordt overschreden?
* Stel wij zetten 20 V over de serieschakeling. Bereken de spanning over de $330 \; \Omega$ weerstand en over de $1000 \; \Omega$ weerstand.
```

```{exercise} 
:class: dropdown
Bekijk figuur {numref}`{number} <fig:II_1:voltdiv>`.
Dit is de (basis)opstelling die gebruikt wordt in dit experiment.
* Leg uit hoe de spanning over de diode bepaald wordt met behulp van deze schakeling.
* Leg uit hoe de stroomsterkte door de diode bepaald wordt met behulp van deze schakeling.
* Bepaal met behulp van bovenstaande twee methodes de onzekerheid in $I_D$ en $U_D$.
```

```{figure} Figures/BM/volt_div.jpg
---
width: 40%
name: fig:II_1:voltdiv
---
De basismeetopstelling bestaat uit de diode en Ohmse weerstand in serie geschakeld met gebruik van twee spanningsmeters.
```

### Methode
In figuur {numref}`{number} <fig:II_1:voltdiv>` is de basisschakeling schematisch getekend. 
De range voor spanning over de diode waarbij de stroomsterkte gemeten moet worden is van $0.1 \; \mathrm{V}$ tot $0.6 \; \mathrm{V}$.
 In dit gebied verandert de stroomsterkte zeer sterk doordat de weerstand van de diode ongeveer 5 decades ($10^5$) groter wordt.
 Bij lage spanningen is de diodeweerstand zeer groot (M$\Omega$) en bij spanningen  rond de $0.6 \; \mathrm{V}$ over de diode is de diodeweerstand klein (h$\Omega$).
 De keuze voor de grootte van de Ohmse weerstand hangt sterk af van de weerstandswaarde van de diode.
Hoe moeten we de waarde van de Ohmse weerstand R$_1$ dan kiezen zodat de spanning over de diode goed te bepalen valt?

Kiezen we een hele grote weerstandswaarde, dan zal de spanningsmeter een merkbare invloed hebben op de gehele schakeling.
Kiezen we een hele kleine weerstandswaarde, dan zal bij zeer lage spanning over de diode, vrijwel alle spanning over de diode staan.
De precieze spanning over de weerstand is dan slecht te bepalen.
De Ohmse weerstand moet dus een grote weerstandswaarde hebben, maar toch veel kleiner dan de interne weerstand van de DMM.
De keuze voor de juiste weerstand is aan jou.
Wel kun je met bovenstaande informatie na gaan wat een goede waarde is als je je bedenkt dat geldt: $U_D=\frac{R_D}{R_D+R_1}U_{\text{bron}}$.

Omdat de weerstandswaarde van de diode zo sterk verschilt, is het lastig om een meetplan op te stellen op basis van een vast interval voor de spanningsbron (bijvoorbeeld van $U_{\text{bron}} = 6.00 \; \mathrm{V}$ tot $0.00 \; \mathrm{V}$ in stappen van $0.25 \; \mathrm{V}$).
Om een gelijke verdeling van metingen over het interessegebied te krijgen, is het verstandig om iteratief te werken.
Dat wil zeggen, voer een meting uit, zet de meting in een script, laat uitrekenen wat de spanning over de diode is, zet de meting in een plot, bepaal op basis daarvan wat de volgende meting moet zijn.
Zo'n aanpak voorkomt een sterke clustering van punten rond $U_D = 0.6 \; \mathrm{V}$ wat de kwaliteit van een fit negatief beïnvloedt.

Een tweede probleem is de stabiliteit van de voeding bij lagere spanningen.
De spanning is dan niet stabiel, en de onzekerheid in de spanning groot. 
Je kunt dit oplossen door gebruik te maken van een tweede spanningsdeler, zie {numref}`{number} figuur <fig:BMopst>`. Doordat de spanning zich deelt over twee weerstanden is de spanning over de diodeschakeling ook kleiner.


```{figure} Figures/BM/BMopstelling.png
---
width: 40%
name: fig:BMopst
---
De meetopstelling bestaat uit de diode en Ohmse weerstand in serie geschakeld met gebruik van twee spanningsmeters.
```

```{exercise}
:class: dropdown
Bekijk {numref}` figuur  {number} <fig:BMopst>`.
* Laat zien dat de spanning over de diodeschakeling gegeven wordt door: $U = \frac{R_3}{R_2+R_3}\cdot U_{bron}$.
* Leg uit dat dit alleen geldt als $R_3 << R_1 + R_D$ 
* Leg uit dat er een extra stap nodig is voor het berekenen van de spanning over de diode.

```

```{exercise}
:class: dropdown
* Schrijf het python script dat je in staat stelt om bovenstaande iteratieve proces uit te voeren. 
Maak gebruik van verschillende cellen: Ruwe data/bewerkte data/plot/fit.
* Zet in het script je berekening voor de onzekerheid in $U_{bron}$, $U_R$ en $R$ klaar.
Deze kan je bij het uitvoeren van het experiment bepalen met behulp van de handleidingen.
* Maak het script voor het vinden van de optimale fit, gebruik daarvoor vergelijking {eq}`eq:stroom_diode`.
* Maak het script voor het berekenen van de constante van Boltzmann op basis van de optimale fit parameters.
* Uit de I-V karakteristiek van een diode kan een grootheid $b$ bepaald worden.
Volgens de theorie geldt: $b=-q/nk_BT$ of $k_B=-q/bnT$.
$q$ is de lading van een elektron (negatief), $n$ de idealiteitsfactor en $T$ de absolute temperatuur.
Als we $b$, $q$, $n$ en $T$ kennen, kunnen we $k_B$ bepalen.
De onzekerheden in $b$, $n$ en $T$ zijn $u(b)$, $u(n)$ en $u(T)$.
Leid een uitdrukking af voor de onzekerheid $u(k_{\text{B}})$ in de gevonden waarde van $k_B$.
```

## Uitvoering (3h)

(subsec:weerstandsmetingen)=
### Weerstandsmetingen
1. Op het perspexpaneel, zie Figuur {numref}`{number} <fig:Boltzman:diode>`, zijn verschillende weerstanden gemonteerd. Noteer de weerstandswaarden in een tabel. Houd ruimte voor twee extra kolommen in de tabel.
2. Meet met behulp van de $3\frac{1}{2}$ digit DMM de weerstanden zo nauwkeurig mogelijk. Noteer de waarden in de tabel.
3. Meet vervolgens met de $5\frac{1}{2}$ digit DMM de weerstandwaarden zo nauwkeurig mogelijk. Noteer ook deze waarden in de tabel. 
4. Vind je dat de waarden gevonden met de $3\frac{1}{2}$ digit DMM en $5\frac{1}{2}$ digit DMM met elkaar overeenstemmen? Waarom? Bereken voor de kleinste weerstand, met behulp van de specificaties van de meters, de nauwkeurigheid van beide metingen. Zijn de waarden strijdig met elkaar? Laat zien.
5. Verdubbel de lengte van de meetsnoeren en meet de waarde de weerstandswaarde opnieuw. Wat heb je hiervan geleerd?

(subsec:spanningsdeler)=
### Spanningsdeler

1. Bouw met de weerstanden op het perspexpaneel schakeling zoals aangegeven in figuur {numref}`{number} <fig:spanningsdeler_spanningsbron>`. Tip: doe dit systematisch aan de hand van het schema. Ben je het overzicht kwijt? Breek alles af en begin opnieuw.
2. Stel de voedingsbron in op ongeveer $20 \; \mathrm{V}$. 
Meet nu de spanning met de $5\frac{1}{2}$ digit meter direct over de voedingsbron ($U_{\text{B}}$), over $R_{1}$ ($V_{\text{AB}}$) en over $R_{\text{2}}$ ($V_{\text{BC}}$). Is $U_B = V_{\text{AB}} + V_{\text{BC}}$ ?
3. Bepaal de verhouding van de spanning over $R_{2}$ ($V_{\text{BC}}$) en de spanning over beide weerstanden $R_{1}$ en $R_{2}$ ($V_{\text{AC}}$). 
Laat zien dat dit klopt met wat we op grond van de gemeten waarden van de weerstanden (al gedaan bij opdracht 4-1) zouden verwachten.
4. Bereken de stroom die door de spanningsdeler loopt.
5. We gaan nu direct de stroom door de spanningsdeler meten met de $3\frac{1}{2}$ digit DMM.
Verander de instelling van de voedingsbron niet (controleer dit met de $5\frac{1}{2}$ digit DMM).
Plaats de stroommeter in het circuit zoals in figuur {numref}`{number} <fig:spanningsdeler_stroommeter>` is aangegeven.
Meet de stroom.
Klopt de gemeten waarde met de berekende waarde?
6. Verlaag de voedingsspanning met een factor 10.
Verander verder niets.
Welke stroom lees je op het $40 \; \mathrm{mA}$ bereik van de $3\frac{1}{2}$ digit DMM af? Schakel over het $4 \; \mathrm{mA}$ bereik van deze DMM. 
Waarom wijkt de nu gevonden waarde af van de waarde op het $40 \; \mathrm{mA}$ bereik? Wat moet je weten om het verschil kwantitatief te verklaren?

```{figure} Figures/BM/spanningsdeler1.jpg
---
width: 30%
name: fig:spanningsdeler_spanningsbron
---
De opstelling voor het meten van de spanningsdeling.
```

```{figure} Figures/BM/spanningsdeler2.jpg
---
width: 30%
name: fig:spanningsdeler_stroommeter
---
De opstelling voor het meten van de stroomsterkte.
```

(subsec:diodemeting)=
### Diodemeting

```{warning} Meten en plotten
Zorg ervoor dat je tijdens de metingen je Python script open hebt staan en dat je na elke meting de nieuwe data invoert en de plot bijwerkt.
Vaak gebeurt het dat studenten pas na de metingen er achter komen dat de metingen niet goed zijn uitgevoerd...
```

* Bouw de opstelling zoals weergegeven in figuur {numref}`{number} <fig:BMopst>`.
Gebruik de 3.5 DMM voor de spanning van de spanningsbron te meten, en de 5.5 voor de meting aan de weerstand die in serie staat met de diode.
* Maak een foto van de opstelling en voeg deze toe aan je labjournaal.
* Voer het iteratieve stappenplan uit.
* Bereken op basis van de functiefit de constante van Boltzmann en de bijbehorende onzekerheid.
* Laat je grafiek en bijbehorende gevonden waarde controleren.
* Ruim de spullen zorgvuldig op.

## Achtergrond

(subsec:geheugensteun)=
### Elektrische schakelingen

Veelal kunnen we een schakeling vereenvoudigen door een serie (of parallel) schakeling van twee weerstanden te vervangen door één weerstand. Als geheugensteuntje geven we hier een samenvatting van de formules die daarbij horen.

```{figure} Figures/BM/serieparallel.png
---
width: 80%
name: fig:serie_parallel
---
Serie en parallelschakeling van twee weerstanden.
Spanningsdeling en stroomdeling.
```
(subsubsec:serieschakeling)=
**Serieschakeling** 

$$
\begin{align}
V_{B} &= V_{1}+V_{2} = I R_{1}+I R_{2}=I\left(R_{1}+R_{2}\right)=I R_{v, s} \rightarrow R_{v, s} =R_{1}+R_{2} \\
\frac{V_{1}}{V_{2}} &= \frac{R_{1}}{R_{2}} \\
V_{2} &= \frac{R_{2}}{R_{1}+R_{2}} V_{B} \quad \text { spanningsdeling }
\end{align}
$$

(subsubsec:parallelschakeling)=
**Parallelschakeling**

$$
\begin{align}
I &=I_{1}+I_{2} = \frac{V_{B}}{R_{1}}+\frac{V_{B}}{R_{2}}=V_{B}\left(\frac{1}{R_{1}}+\frac{1}{R_{2}}\right)=V_{B} \frac{1}{R_{v, p}} \rightarrow \frac{1}{R_{v, p}}=\frac{1}{R_{1}}+\frac{1}{R_{2}} \\ 
\frac{I_{1}}{I_{2}} &=\frac{R_{2}}{R_{1}} \\ 
I_{2} &=\frac{R_{1}}{R_{1}+R_{2}} I \quad \text { stroomdeling }
\end{align}
$$

(subsubsec:gedissipeerd_vermogen)=
**Gedissipeerd vermogen**

$$
P=V I=\frac{V^{2}}{R}=I^{2} R
$$

(subsec:halfgeleiderdiode2)=
### Halfgeleiderdiode

```{iframe} https://www.youtube.com/embed/AF8d72mA41M?si=hejU74ZWfVCubk2I
```

Bovenstaande Veritasium clip legt op een zeer gedegen manier de werking van een diode (hier dan een LED) uit.
Alhoewel het gehele filmpje de moeite waard is, begint de uitleg over de werking rond 4:00.

Om de werking van een halfgeleiderdiode goed te begrijpen is een behoorlijke kennis van het gedrag van elektronen in halfgeleiders nodig.
Dit onderwerp komt pas in het tweede of derde studiejaar aan de orde en dan is het nog niet zo eenvoudig.
Voor de uitvoering van de proef is het niet noodzakelijk de werking van een diode te kennen.
Omdat het voor velen onbevredigend is met iets te werken waarvan je niet weet hoe het werkt, laten wij hier eerst zien, hoe we met niet zo heel veel voorkennis, kunnen inzien waarom een halfgeleiderdiode in de ene stroomrichting wel en in de andere stroomrichting niet geleidt.


(subsubsec:werking)=
**Werking**

1. Uiterst zuiver halfgeleider materiaal heeft bij lage temperatuur (b.v. kamertemperatuur of lager voor Si) zeer weinig vrije ladingsdragers en is daardoor een zeer slechte stroomgeleider.
2. De geleiding kan sterk worden verhoogd door het toevoegen van vreemde atomen.
Dit wordt dotering of doping genoemd.
3. Voegen we aan Si een 5-waardig element toe, b.v. P, As of Sb, dan heeft dit element sterk de neiging één elektron los te laten.
Dit elektron gedraagt zich als een vrij elektron en het zijn deze elektronen die ervoor zorgen dat in dit "n-type" materiaal, wel stroomgeleiding kan plaatsvinden.
4. Voegen we aan Si een 3-waardig element toe, b.v. B, dan heeft dit element sterk de neiging een elektron van een Si atoom te binden.
Door dit proces ontstaat er een "gat" in de elektronen omringing van het Si atoom.
Dit gat kan weer opgevuld worden door een elektron van een ander Si atoom, enz.
Op deze manier beweegt het gat als het ware vrij door het materiaal.
Het gat gedraagt zich als een positieve ladingsdrager.
Het zijn de gaten die ervoor zorgen dat stroomgeleiding in dit "p-type" materiaal kan plaatsvinden.


```{figure} Figures/BM/halfgeleiderstroom.png
---
width: 60%
name: fig:stroom_door_halfgeleider
---
Stroom door een halfgeleiderdiode. 
De pluspool van een spanningsbron is aangesloten op het p-type materiaal en de minpool op het n-type materiaal. 
Door recombinatie van gaten en elektronen nabij het grensvlak kan de stroom blijven lopen.
```

Daar gebeurt iets bijzonders: de arriverende elektronen vallen in de arriverende gaten.
Dit wordt recombinatie genoemd.
Hierdoor raken we twee vrije ladingsdragers kwijt.
Echter, door de aanwezigheid van de spanningsbron worden steeds nieuwe gaten en elektronen aangevoerd.
Door dit proces ontstaat er een constante gaten (en elektronen) stroom naar het grensvlak.
Van buiten af gezien denk je dat er gewoon een stroom van de plus naar de minpool loopt.
Wij zeggen dat de diode in voorwaartse richting is geschakeld.
Nu sluiten we de minpool van de spanningsbron aan op het p-type en de pluspool aan op het n-type materiaal. <!--(zie Fig. {!!!!!!}) -->

```{figure} Figures/BM/halfgeleiderstroom2.png
---
width: 60%
name: fig:minpool_spanningsbron
---
De minpool van een spanningsbron is aangesloten op het p-type materiaal en de pluspool is op het n-type materiaal.
Er kan nu geen stroom lopen omdat er een gebied zonder vrije ladingsdragers wordt gevormd.
```

Dit is niet het hele verhaal.
Zoals we weten hebben de elektronen (en gaten) niet allemaal dezelfde energie.
In een halfgeleider is de energie van de elektronen (gaten) verdeeld volgens de Boltzmann verdeling.
De gemiddelde energie van een elektron (gat) is $k_{\text{B}} T$ ($T$ is de absolute temperatuur en $k_B$ is de Boltzmann constante).
Het hangt nu van de hoogte van de barrière ten opzichte van $k_{\text{B}} T$ af hoeveel elektronen (gaten) er over de barrière kunnen komen en dus hoeveel stroom er kan gaan lopen.
De hoogte van de barrière wordt mede bepaald door de grootte van de voorwaartse spanning.
Hoe hoger de voorwaartse spanning des te lager de barrière.

## Materialen


```{figure} Figures/Boardje2.jpg
---
width: 70%
name: fig:Boltzman:diode
---
Het elektronica boardje en de schematische weergave ervan.
```