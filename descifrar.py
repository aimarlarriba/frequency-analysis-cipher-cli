import sys
from collections import Counter

# Tabla de frecuencias del español (porcentajes)
frecuencias_espanol = {
    'e': 16.78, 'a': 11.96, 'o': 8.69, 'l': 8.37, 's': 7.88,
    'n': 7.01, 'd': 6.87, 'r': 4.94, 'u': 4.80, 'i': 4.15,
    't': 3.31, 'c': 2.92, 'p': 2.776, 'm': 2.12, 'y': 1.54,
    'q': 1.53, 'b': 0.92, 'h': 0.89, 'g': 0.73, 'f': 0.52,
    'v': 0.39, 'j': 0.30, 'ñ': 0.29, 'z': 0.15, 'x': 0.06,
    'k': 0.0, 'w': 0.0
}

ALFABETO = [chr(i) for i in range(ord('a'), ord('z')+1)] + ['ñ']

def calcular_porcentajes(texto: str) -> dict:
    filtrado = [c.lower() for c in texto if c.isalpha()]
    total = len(filtrado)
    contador = Counter(filtrado)
    return {letra: (contador[letra] / total) * 100 for letra in contador}

def crear_mapa(texto: str, manuales: dict = None) -> dict:
    """Crea un mapa de sustitución incluyendo todas las letras del alfabeto."""
    porcentajes_texto = calcular_porcentajes(texto)
    letras_cifradas = sorted(porcentajes_texto, key=lambda x: -porcentajes_texto[x])

    # Añadimos las letras del alfabeto que no aparezcan en el texto
    for letra in ALFABETO:
        if letra not in letras_cifradas:
            letras_cifradas.append(letra)

    letras_espanol = [k for k, _ in sorted(frecuencias_espanol.items(), key=lambda x: -x[1])]

    mapa = {}
    usadas = set()

    # primero ponemos las manuales
    if manuales:
        for cif, real in manuales.items():
            mapa[cif] = real
            usadas.add(real)

    # luego asignamos las restantes por frecuencia
    for cif in letras_cifradas:
        if cif in mapa:
            continue
        for letra in letras_espanol:
            if letra not in usadas:
                mapa[cif] = letra
                usadas.add(letra)
                break
    return mapa

def descifrar(texto: str, mapa: dict) -> str:
    resultado = ""
    for c in texto:
        if c.isalpha():
            resultado += mapa.get(c.lower(), c.lower())
        else:
            resultado += c
    return resultado

def mostrar_mapa(mapa: dict):
    print("\nMapa de sustituciones actual:")
    for cif, real in sorted(mapa.items()):
        print(f"  {cif} → {real}")
    print("-" * 40)

def descifrado_interactivo(texto_cifrado: str):
    manuales = {}
    mapa = crear_mapa(texto_cifrado, manuales)

    while True:
        texto_descifrado = descifrar(texto_cifrado, mapa)
        print("\nTexto descifrado provisional:")
        print(texto_descifrado)

        mostrar_mapa(mapa)

        resp = input("\n¿Es correcto? (s/n): ").strip().lower()
        if resp == "s":
            print("\n✔ Descifrado final:")
            print(texto_descifrado)
            break
        else:
            entrada = input("Introduce equivalencias manuales (ejemplo: x=e k=a). Enter para ninguna: ").strip().lower()
            if entrada:
                pares = entrada.split()
                for par in pares:
                    if "=" in par:
                        cif, real = par.split("=")
                        cif, real = cif.strip(), real.strip()
                        if len(cif) == 1 and len(real) == 1:
                            manuales[cif] = real
                        else:
                            print(f"❌ Formato inválido: {par}")
            # recalculamos el mapa respetando las manuales
            mapa = crear_mapa(texto_cifrado, manuales)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 descifrar.py \"TEXTO_CIFRADO\"")
        sys.exit(1)

    texto_cifrado = sys.argv[1]
    descifrado_interactivo(texto_cifrado)

