# Koodikaveri Bot

Koodikaveri Bot on Discord-botti, joka tarjoaa ohjelmointiopastusta ja tietoa eri ohjelmointikielistä. Botilla on myös komentoja, joilla voit etsiä vastauksia Stack Overflowsta ja hakea dokumentaatiota eri teknologioista.

## Ominaisuudet

- **Ohjelmointikielten komennot**: Tietoa ja esimerkkejä ohjelmointikielistä, kuten Python, JavaScript, HTML, CSS ja React.
- **Stack Overflow -haku**: Hakee kysymyksiä ja vastauksia Stack Overflowsta.
- **Dokumentaation haku**: Hakee dokumentaatiolinkkejä ohjelmointikielille ja kehyksille.
- **Koodin esimerkit**: Näyttää esimerkkikoodia eri kielillä.
- **Koodin tarkistus**: Tarkistaa koodinpätkien syntaksin.
- **Tervetuloa- komento**: Lähettää tervetuloviestejä uusille jäsenille.

## Käyttöönotto

### Ympäristömuuttujat

Luo `.env`-tiedosto projektin juureen ja lisää seuraava ympäristömuuttuja:

    DISCORD_TOKEN=your_discord_bot_token


**Huom:** Älä koskaan tallenna `.env`-tiedostoa versionhallintaan. Lisää se `.gitignore`-tiedostoon.

### Asennus

1. **Kloonaa Repositorio:**

    ```
    git clone https://github.com/micsno/koodikaveri.git
    cd koodikaveri
    ```

2. **Luo Virtuaaliympäristö** (valinnainen, mutta suositeltava):

    ```
    python -m venv venv
    ```

    Aktivoi virtuaaliympäristö:

    - **Linux/macOS:**
      ```
      source venv/bin/activate
      ```

    - **Windows:**
      ```
      venv\Scripts\activate
      ```

3. **Asenna Riippuvuudet:**

    ```
    pip install -r requirements.txt
    ```

## Käynnistä Bottisi

1. **Käynnistä Bottisi Paikallisesti:**

    ```
    python bot.py
    ```

## Komennot

- `!ping`: Vastaa 'Pong!' muodossa ` ```Pong!``` `
- `!react`: Näyttää tietoa React-kirjastosta.
- `!react_native`: Näyttää tietoa React Native -kirjastosta.
- `!javascript`: Näyttää tietoa JavaScript-kielestä.
- `!html`: Näyttää tietoa HTML:stä.
- `!css`: Näyttää tietoa CSS:stä.
- `!python`: Näyttää tietoa Python-kielestä.
- `!kysy <kysymys>`: Hakee ja palauttaa kysymyksen Stack Overflowsta.
- `!fetch_answer <URL>`: Hakee ja näyttää ensimmäisen löydetyn `<p>`-tagin sisällön annetusta URL:stä.
- `!docs <kieli> <haku>`: Hakee tietyn ohjelmointikielen tai kirjaston dokumentaatiosta annettua hakusanaa.
- `!koodipohja <kieli>`: Näyttää yleisen koodipohjan annetulla ohjelmointikielellä.
- `!tarkista <koodi>`: Tarkistaa annetun koodinpätkän syntaktisen oikeellisuuden.
- `!ohje`: Näyttää ohjeet botin käyttöön.

## Lisenssi

Tämä projekti on lisensoitu MIT-lisenssillä. Katso [LICENSE](LICENSE) tiedosto lisenssin yksityiskohtia varten.

## Yhteystiedot

Jos sinulla on kysyttävää botista tai tarvitset apua, ota yhteyttä [micsno@pm.me].
