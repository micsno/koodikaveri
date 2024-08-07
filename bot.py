import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Tervetuloa, {member.mention}, {guild.name}-palvelimelle! Käytä `!ohje` saadaksesi ohjeet botin käyttöön.'
        await guild.system_channel.send(to_send)

@bot.command()
async def ping(ctx):
    await ctx.send('```\nPong!\n```')

@bot.command()
async def react(ctx):
    response = """
React on JavaScript-kirjasto, jonka avulla voit rakentaa käyttäjärajapintoja.
- Aloita komponenttien luomisesta.
- Käytä JSX-syntaksia HTML-elementtien määrittämiseen.
- Hallitse tilaa (state) ja rekvisiittaa (props) komponenttien välillä.
Virallinen dokumentaatio: https://reactjs.org/docs/getting-started.html
"""
    await ctx.send(response)

@bot.command()
async def javascript(ctx):
    response = """
JavaScript on monipuolinen ohjelmointikieli web-kehitykseen.
- Muista, että JavaScript on asynkroninen ja tapahtumapohjainen.
- Käytä let ja const avainsanoja muuttujien määrittämiseen.
- Tutustu moderneihin ES6+ ominaisuuksiin kuten nuolifunktioihin ja luokkiin.
MDN-dokumentaatio: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
"""
    await ctx.send(response)

@bot.command()
async def html(ctx):
    response = """
HTML (HyperText Markup Language) on verkkosivujen rakennekieli.
- Käytä erilaisia tageja (esim. <div>, <p>, <a>) määrittämään sivun rakenne.
- Muista käyttää semanttisia tageja (esim. <header>, <footer>, <article>).
- Käytä attribuutteja (esim. class, id) määrittämään elementtien ominaisuuksia.
Virallinen dokumentaatio: https://developer.mozilla.org/en-US/docs/Web/HTML
"""
    await ctx.send(response)

@bot.command()
async def css(ctx):
    response = """
CSS (Cascading Style Sheets) käytetään verkkosivujen tyylittämiseen.
- Käytä selektoreita (esim. .class, #id, element) valitaksesi elementtejä.
- Käytä erilaisia ominaisuuksia (esim. color, margin, padding) määrittämään tyylejä.
- Tutustu flexboxiin ja CSS Grid:iin luodaksesi joustavia ja reagoivia asetteluja.
MDN-dokumentaatio: https://developer.mozilla.org/en-US/docs/Web/CSS
"""
    await ctx.send(response)

@bot.command()
async def python(ctx):
    response = """
Python on korkean tason ohjelmointikieli, joka tunnetaan selkeydestään ja luettavuudestaan.
- Muista käyttää sisennystä koodin lohkojen erottamiseen.
- Käytä erilaisia tietorakenteita kuten listat, tuple ja sanakirjat.
- Tutustu Pythonin standardikirjastoon laajentaaksesi ohjelmointimahdollisuuksia.
Virallinen dokumentaatio: https://docs.python.org/3/
"""
    await ctx.send(response)

@bot.command()
async def react_native(ctx):
    response = """
React Native on JavaScript-kehys, joka mahdollistaa mobiilisovellusten kehittämisen käyttämällä Reactiä.
- Käytä komponentteja luodaksesi natiivielementtejä.
- Hyödynnä Reactin osaamista ja kirjoita mobiilisovelluksia.
- Yhdistä natiiviin koodiin tarvittaessa.
Virallinen dokumentaatio: https://reactnative.dev/docs/getting-started
"""
    await ctx.send(response)

@bot.command()
async def kysy(ctx, *, query):
    response = requests.get(f'https://api.stackexchange.com/2.3/search/advanced',
                            params={'order': 'desc', 'sort': 'relevance', 'q': query, 'site': 'stackoverflow'})
    data = response.json()
    if not data['items']:
        await ctx.send('En löytänyt kysymystäsi vastaavaa kysymystä Stack Overflowsta.')
    else:
        top_result = data['items'][0]
        answer_url = top_result['link']
        await ctx.send(f'Tässä on parhaiten vastaava kysymys Stack Overflowssa: {answer_url}')

@bot.command()
async def fetch_answer(ctx, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        answer = soup.find('p').get_text() if soup.find('p') else 'Ei löytynyt vastausta.'
        await ctx.send(f'```\nVastaus linkistä {url}:\n{answer}\n```')
    except requests.RequestException as e:
        await ctx.send(f'```\nVirhe haettaessa linkistä: {e}\n```')

@bot.command()
async def docs(ctx, language: str, query: str):
    docs_urls = {
        'python': f'https://docs.python.org/3/search.html?q={query}',
        'javascript': f'https://developer.mozilla.org/en-US/search?q={query}',
        'react': f'https://reactjs.org/search?q={query}',
        'react_native': f'https://reactnative.dev/docs/search?q={query}',
        'html': f'https://developer.mozilla.org/en-US/search?q={query}&topic=html',
        'css': f'https://developer.mozilla.org/en-US/search?q={query}&topic=css'
    }
    if language.lower() in docs_urls:
        await ctx.send(f'Linkki {language} dokumentaatioon: {docs_urls[language.lower()]}')
    else:
        await ctx.send('En löytänyt annettua ohjelmointikieltä tai kirjastoa.')

@bot.command()
async def koodipohja(ctx, language: str):
    code_snippets = {
        'python': """```python
def hello_world():
    print("Hello, world!")

if __name__ == "__main__":
    hello_world()
```""",
        'javascript': """```javascript
function helloWorld() {
    console.log("Hello, world!");
}

helloWorld();
```""",
        'react': """```javascript
import React from 'react';

class HelloWorld extends React.Component {
    render() {
        return <h1>Hello, world!</h1>;
    }
}

export default HelloWorld;
```""",
        'react_native': """```javascript
import React from 'react';
import { Text, View } from 'react-native';

const HelloWorld = () => {
    return (
        <View>
            <Text>Hello, world!</Text>
        </View>
    );
};

export default HelloWorld;
```""",
        'html': """```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello, world!</title>
</head>
<body>
    <h1>Hello, world!</h1>
</body>
</html>
```""",
        'css': """```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    color: #333;
}
h1 {
    color: #007bff;
}
```"""
    }
    if language.lower() in code_snippets:
        await ctx.send(code_snippets[language.lower()])
    else:
        await ctx.send('En löytänyt annettua ohjelmointikieltä tai kirjastoa.')

@bot.command()
async def tarkista(ctx, *, code: str):
    try:
        exec(code)
        await ctx.send('Koodi on syntaktisesti oikein.')
    except SyntaxError as e:
        await ctx.send(f'Koodi sisältää syntaksivirheitä: {e}')
    except Exception as e:
        await ctx.send(f'Koodi sisältää virheitä: {e}')

@bot.command()
async def ohje(ctx):
    help_message = """
**Ohjeet Koodikaverin Käyttöön:**

**Komennot:**
- `!ping`: Vastaa 'Pong!' muodossa ` ```Pong!``` `
- `!react`: Näyttää React-kirjastosta tietoa.
- `!react_native`: Näyttää React Native -kirjastosta tietoa.
- `!javascript`: Näyttää JavaScript-kielestä tietoa.
- `!html`: Näyttää HTML:stä tietoa.
- `!css`: Näyttää CSS:stä tietoa.
- `!python`: Näyttää Python-kielestä tietoa.
- `!kysy <kysymys>`: Hakee ja palauttaa Stack Overflowsta kysymyksen, joka vastaa hakusanaasi.
- `!fetch_answer <URL>`: Hakee ja näyttää ensimmäisen löydetyn <p>-tagin sisällön annetusta URL:stä.
- `!docs <kieli> <haku>`: Hakee tietyn ohjelmointikielen tai kirjaston dokumentaatiosta annettua hakusanaa.
- `!koodipohja <kieli>`: Näyttää yleisen koodipohjan annetulla ohjelmointikielellä.
- `!tarkista <koodi>`: Tarkistaa annetun koodinpätkän syntaktisen oikeellisuuden.

**Huomautuksia:**
- Huom: Vastaukset on haettu linkin takaa Stack Overflowsta. Tarkista vastaus ja lähteet tarvittaessa.

Jos sinulla on kysyttävää botin toiminnasta tai sen käytöstä, älä epäröi kysyä!
"""
    await ctx.send(help_message)

bot.run(TOKEN)
