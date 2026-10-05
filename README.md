# Frequency Analysis Cryptanalysis CLI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version"/>
  <img src="https://img.shields.io/badge/Domain-Classical%20Cryptography-red?style=for-the-badge" alt="Domain"/>
  <img src="https://img.shields.io/badge/Architecture-Interactive%20CLI%20REPL-blue?style=for-the-badge" alt="CLI REPL"/>
  <img src="https://img.shields.io/badge/Dependencies-Zero%20Dependencies-brightgreen?style=for-the-badge" alt="Zero Dependencies"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License"/>
</p>

---

## 📌 Resumen del Proyecto

**Frequency Analysis Cryptanalysis CLI** es una herramienta en Python diseñada para el **criptoanálisis interactivo de cifrados por sustitución monoalfabética** mediante el estudio de distribuciones de frecuencia de caracteres en el idioma español.

Los cifrados clásicos de sustitución monoalfabética preservan la signatura lingüística y la entropía del idioma original. Esta herramienta automatiza la correspondencia estadística de máxima verosimilitud entre las frecuencias observadas en el criptograma y el corpus de referencia de la lengua española (RAE/Cervantes), proporcionando un **entorno REPL interactivo** para que el analista realice ajustes finos de equivalencias en tiempo real.

---

## 🚀 Características Principales

* 📊 **Mapeo Heurístico Automatizado:** Calcula las frecuencias relativas del criptograma y genera un primer mapa de sustitución basado en la curva de frecuencias del español (`E`, `A`, `O`, `L`, `S`...).
* 🛠️ **Consola Interactiva (Human-in-the-Loop):** Permite fijar pares manuales de letras (`x=e`, `k=a`) y recalcula automáticamente la redistribución del resto del alfabeto.
* 🔠 **Preservación de Formato:** Mantiene la capitalización original (mayúsculas/minúsculas), signos de puntuación, saltos de línea y caracteres especiales.
* ⚡ **Cero Dependencias Externas:** Desarrollado íntegramente sobre la **librería estándar de Python** (`collections`, `argparse`, `typing`).
* 📁 **Soporte CLI Flexible:** Admite texto directo por argumentos, lectura de archivos de texto (`-f / --file`) o modo desatendido (`--auto`).

---

## 🧮 Fundamento Criptográfico

En cualquier texto extenso en español, la distribución de frecuencias de las letras no es uniforme, sino que exhibe un patrón característico:

| Carácter | Frecuencia Relativa (%) | Carácter | Frecuencia Relativa (%) |
| :---: | :---: | :---: | :---: |
| **E** | 16.78% | **D** | 6.87% |
| **A** | 11.96% | **R** | 4.94% |
| **O** | 8.69% | **U** | 4.80% |
| **L** | 8.37% | **I** | 4.15% |
| **S** | 7.88% | **T** | 3.31% |
| **N** | 7.01% | **C** | 2.92% |

El script contabiliza las apariciones en el texto cifrado, calcula porcentajes de aparición y asigna como hipótesis inicial las letras más comunes del castellano a los símbolos más frecuentes observados.

---

## ⚙️ Instalación y Uso Rápido

### 1. Clonar el repositorio
```bash
git clone https://github.com/aimarlarriba/frequency-analysis-cipher-cli.git
cd frequency-analysis-cipher-cli
```

### 2. Modos de Ejecución

#### A) Modo Interactivo Asistido (Recomendado)
Analizar un archivo de texto cifrado con el asistente interactivo:
```bash
python descifrar.py -f samples/cifrado_quijote.txt
```

#### B) Modo Directo por Argumento
```bash
python descifrar.py "Kk ec vemxo tk vx Bxkpjx..."
```

#### C) Modo Automático Desatendido (`--auto`)
Para pipelines o scripts que requieran el texto descifrado directamente por salida estándar:
```bash
python descifrar.py -f samples/cifrado_quijote.txt --auto
```

---

## 🖥️ Ejemplo de Sesión Interactiva

```text
======================================================
Cifrada   Freq Obs (%)   Sustitución    Ref Español (%)
------------------------------------------------------
x         14.85          e              16.78          
k         11.22          a              11.96          
r         9.15           o              8.69           
...
======================================================

--- TEXTO DESCIFRADO PROVISIONAL ---
En un lugar de la Mancha, de cuyo nombre no quiero acordarme...

¿El descifrado es correcto y legible? (s/n): n

Introduce correcciones (ej: 'x=e' o varias 'x=e z=a').
> x=e k=a
```

---

## 🧪 Pruebas Automatizadas

El proyecto incluye tests unitarios para verificar el motor de conteo estadístico, el mapeo condicional y la conservación de caracteres:
```bash
python -m unittest discover tests
```

---

## 👥 Contexto Académico

Desarrollado originalmente como trabajo práctico para la asignatura de **Seguridad y Gestión de la Seguridad de Sistemas de Información (SGSSI)** en la **Universidad del País Vasco (UPV/EHU)**. 

Refactorizado, modularizado y mantenido por **[Aimar Larriba](https://github.com/aimarlarriba)** como utilidad didáctica de criptoanálisis clásico.

---

## ⚖️ Licencia

Distribuido bajo la Licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.
