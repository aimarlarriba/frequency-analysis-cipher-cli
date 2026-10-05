"""
Herramienta de Criptoanálisis por Análisis de Frecuencias para Cifrados de Sustitución Monoalfabética.
Soporta interactividad, ajuste heurístico guiado y preservación de formato y mayúsculas.
"""

import sys
import argparse
from collections import Counter
from typing import Dict, List, Optional


# Frecuencias relativas de letras en el idioma español (referencia estadística estándar)
FRECUENCIAS_ESPANOL: Dict[str, float] = {
    'e': 16.78, 'a': 11.96, 'o': 8.69, 'l': 8.37, 's': 7.88,
    'n': 7.01,  'd': 6.87,  'r': 4.94, 'u': 4.80, 'i': 4.15,
    't': 3.31,  'c': 2.92,  'p': 2.77, 'm': 2.12, 'y': 1.54,
    'q': 1.53,  'b': 0.92,  'h': 0.89, 'g': 0.73, 'f': 0.52,
    'v': 0.39,  'j': 0.30,  'ñ': 0.29, 'z': 0.15, 'x': 0.06,
    'k': 0.01,  'w': 0.01
}

ALFABETO_ESPANOL: List[str] = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['ñ']


def calcular_frecuencias(texto: str) -> Dict[str, float]:
    """Calcula la frecuencia porcentual de cada letra en el texto proporcionado."""
    filtrado = [c.lower() for c in texto if c.isalpha()]
    total = len(filtrado)
    if total == 0:
        return {}
    contador = Counter(filtrado)
    return {letra: (contador[letra] / total) * 100 for letra in contador}


def crear_mapa_sustitucion(texto: str, manuales: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    """
    Construye el mapa de sustitución emparejando la frecuencia del texto
    cifrado con la distribución estadística del español, respetando las asignaciones fijadas.
    """
    frecuencias_texto = calcular_frecuencias(texto)
    letras_cifradas = sorted(frecuencias_texto, key=lambda x: -frecuencias_texto[x])

    for letra in ALFABETO_ESPANOL:
        if letra not in letras_cifradas:
            letras_cifradas.append(letra)

    letras_espanol = [k for k, _ in sorted(FRECUENCIAS_ESPANOL.items(), key=lambda x: -x[1])]

    mapa: Dict[str, str] = {}
    usadas = set()

    # 1. Asignaciones manuales
    if manuales:
        for cif, real in manuales.items():
            mapa[cif] = real
            usadas.add(real)

    # 2. Asignación estadística restante
    for cif in letras_cifradas:
        if cif in mapa:
            continue
        for letra in letras_espanol:
            if letra not in usadas:
                mapa[cif] = letra
                usadas.add(letra)
                break

    return mapa


def descifrar_texto(texto: str, mapa: Dict[str, str], preservar_mayusculas: bool = True) -> str:
    """Aplica el mapa de sustitución sobre el texto manteniendo puntuación y casing original."""
    resultado = []
    for c in texto:
        if c.isalpha():
            caracter_base = c.lower()
            sustituto = mapa.get(caracter_base, caracter_base)
            if preservar_mayusculas and c.isupper():
                resultado.append(sustituto.upper())
            else:
                resultado.append(sustituto)
        else:
            resultado.append(c)
    return "".join(resultado)


def imprimir_tabla_frecuencias(frecuencias_texto: Dict[str, float], mapa: Dict[str, str]):
    """Imprime una tabla comparativa de frecuencias en consola."""
    print("\n" + "=" * 54)
    print(f"{'Cifrada':<10}{'Freq Obs (%)':<15}{'Sustitución':<15}{'Ref Español (%)':<15}")
    print("-" * 54)
    for cif, freq in sorted(frecuencias_texto.items(), key=lambda x: -x[1])[:15]:
        real = mapa.get(cif, "?")
        ref_freq = FRECUENCIAS_ESPANOL.get(real, 0.0)
        print(f"{cif:<10}{freq:<15.2f}{real:<15}{ref_freq:<15.2f}")
    print("=" * 54 + "\n")


def descifrado_interactivo(texto_cifrado: str):
    """Bucle REPL interactivo para asistir al analista criptográfico."""
    manuales: Dict[str, str] = {}
    frecuencias = calcular_frecuencias(texto_cifrado)

    while True:
        mapa = crear_mapa_sustitucion(texto_cifrado, manuales)
        texto_descifrado = descifrar_texto(texto_cifrado, mapa)

        print("\n" + "#" * 60)
        print("--- TEXTO DESCIFRADO PROVISIONAL ---")
        print(texto_descifrado[:350] + ("..." if len(texto_descifrado) > 350 else ""))
        print("#" * 60)

        imprimir_tabla_frecuencias(frecuencias, mapa)
        if manuales:
            print("Fijadas manualmente:", ", ".join([f"{k} -> {v}" for k, v in manuales.items()]))

        resp = input("\n¿El descifrado es correcto y legible? (s/n): ").strip().lower()
        if resp in ("s", "si", "y", "yes"):
            print("\n✔ RESULTADO FINAL COMPLETO:")
            print("-" * 60)
            print(texto_descifrado)
            print("-" * 60)
            break
        else:
            print("\nIntroduce correcciones (ej: 'x=e' o varias 'x=e z=a').")
            print("Escribe 'reset' para reiniciar o presiona Enter para recalcular:")
            entrada = input("> ").strip().lower()
            if entrada == "reset":
                manuales.clear()
                continue
            if entrada:
                pares = entrada.split()
                for par in pares:
                    if "=" in par:
                        partes = par.split("=")
                        cif, real = partes[0].strip(), partes[1].strip()
                        if len(cif) == 1 and len(real) == 1:
                            manuales[cif] = real
                        else:
                            print(f"❌ Formato inválido ignorado: '{par}'")


def main():
    parser = argparse.ArgumentParser(
        description="Herramienta de Criptoanálisis de Cifrados por Sustitución (Frecuencias del Español)."
    )
    parser.add_argument("texto", nargs="?", help="Texto cifrado a analizar.")
    parser.add_argument("-f", "--file", help="Ruta a un archivo .txt con el texto cifrado.")
    parser.add_argument("--auto", action="store_true", help="Modo no interactivo: descifra automáticamente por máxima verosimilitud estadística.")

    args = parser.parse_args()

    texto = ""
    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                texto = f.read()
        except Exception as e:
            print(f"Error al leer archivo {args.file}: {e}")
            sys.exit(1)
    elif args.texto:
        texto = args.texto
    else:
        print("Introduce el texto cifrado a continuación (Presiona Enter para finalizar):")
        texto = sys.stdin.readline().strip()

    if not texto.strip():
        print("Error: No se proporcionó texto para descifrar.")
        sys.exit(1)

    if args.auto:
        mapa = crear_mapa_sustitucion(texto)
        resultado = descifrar_texto(texto, mapa)
        print(resultado)
    else:
        descifrado_interactivo(texto)


if __name__ == "__main__":
    main()
