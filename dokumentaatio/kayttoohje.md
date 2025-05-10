# Käyttöohje #
Lataa projektin viimeisimmän [releasen]() lähdekoodi valitsemalla _Assets_-osion alta _Source code_.
## Käynnistys ##

Asennetaan riippuvuudet:
```bash
poetry install
```
Alustetaan sovellus:
```bash
poetry run invoke build
```
Käynnistetään ohjelma:
```
poetry run invoke start
```


## Sovelluksen käyttö ##
Sovellus käynnistyy aloitusnäkymään, josta voit siirtyä luomaan käyttäjän tai kirjautumaan sisään.

## Uuden käyttäjän luonti ##
Painettuasi "Rekisteröidy" nappia pääset laittamaan itsellesi käyttäjätunnuksen, millä jatkossa kirjautua sisään. Tämän jälkeen paina "Luo käyttäjä", joka kirjaa sinut automaattisesti sisään.

## Kirjautuminen sisään ##
Painettuasi "Kirjaudu sisään" nappia, pitää sinun syöttää aiemmin luomasi käyttäjätunnus. Tämän jälkeen pääset "Kirjaudu sisään" napista katselemaan omaa sivuasi. Mikäli käyttäjänimesi on väärin, ilmoitetaan siitä näkymässä.

## Postauksen teko ##
Kun olet kirjautuneena sisään, voit kirjoittaa postauksen avoimeen tekstikenttään. Paina tämän jälkeen "Lähetä kirjaus" nappia, jonka avulla postauksesi listaantuu sivulle. Jokaisen postauksen kohdalla on poisto nappi, mikä poistaa kyseisen kirjauksen. Kun olet valmis, "Kirjaudu ulos" nappi vie sinut aloitussivulle.