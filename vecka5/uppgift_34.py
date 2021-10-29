import webbrowser
from pathlib import Path

OUTPUT_PATH = Path("djur.html")

# DEFINIERA CLASS Djur!


if __name__ == '__main__':
    djur = []
    zebra = Djur('Zebra', False, 'https://sv.wikipedia.org/wiki/Zebror')
    tiger = Djur('Tiger', True, 'https://sv.wikipedia.org/wiki/Tiger')
    djur.append(zebra)
    djur.append(tiger)
    html = '<html><table>'
    for d in djur:
        cell_2 = 'Vegetarian'
        if d.carnivore:
            'Köttätare'
        html += f'<tr><td><a href="{d.wiki_url}">{d.name}</td><td>{cell_2}</td></tr>\n'
    html += '</table></html>'
    OUTPUT_PATH.write_text(html, encoding='utf8')
    webbrowser.open(str(OUTPUT_PATH))