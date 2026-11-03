import json
import re
from datetime import date

INICIO = date(2026, 1, 5)  

with open("recomendaciones.json", encoding="utf-8") as f:
    lista = json.load(f)

semanas = (date.today() - INICIO).days // 7
rec = lista[semanas % len(lista)]

bloque = (
    "<!-- RECOMENDACION:START -->\n"
    f"**{rec['titulo']}** · {rec['tipo']}\n"
    f"{rec['descripcion']} · [Ver]({rec['link']})\n"
    "<!-- RECOMENDACION:END -->"
)

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

nuevo = re.sub(
    r"<!-- RECOMENDACION:START -->.*?<!-- RECOMENDACION:END -->",
    lambda _: bloque,
    readme,
    flags=re.DOTALL,
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(nuevo)
