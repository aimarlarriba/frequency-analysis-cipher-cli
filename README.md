[🇬🇧 English](README.md) | [🇪🇸 Español](README.es.md)

# Frequency Analysis Cryptanalysis CLI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version"/>
  <img src="https://img.shields.io/badge/Domain-Classical%20Cryptography-red?style=for-the-badge" alt="Domain"/>
  <img src="https://img.shields.io/badge/Architecture-Interactive%20CLI%20REPL-blue?style=for-the-badge" alt="CLI REPL"/>
  <img src="https://img.shields.io/badge/Dependencies-Zero%20Dependencies-brightgreen?style=for-the-badge" alt="Zero Dependencies"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License"/>
</p>

---

## 📌 Project Overview

**Frequency Analysis Cryptanalysis CLI** is a lightweight, interactive Python tool engineered for the **heuristic cryptanalysis of monoalphabetic substitution ciphers** using linguistic letter frequency distributions in the Spanish language.

Classical monoalphabetic ciphers preserve the underlying language entropy and character signature. This utility automates the initial maximum-likelihood statistical matching between observed ciphertext symbol frequencies and the baseline Spanish corpus distribution (RAE/Cervantes corpus), while providing an interactive **Human-in-the-Loop REPL environment** for real-time substitution refinement and key recovery.

---

## 🚀 Key Features

* 📊 **Automated Statistical Mapping:** Computes relative letter frequencies in the ciphertext and establishes a maximum-likelihood substitution mapping using standard Spanish corpus distributions (`E`, `A`, `O`, `L`, `S`...).
* 🛠️ **Interactive REPL Assistant:** Dynamic terminal console allowing the analyst to fix known character pairs (`x=e`, `k=a`) and automatically recompute remaining alphabet mappings on the fly.
* 🔠 **Format & Case Preservation:** Fully preserves original casing (uppercase/lowercase), punctuation, accents, line breaks, and whitespace.
* ⚡ **Zero External Dependencies:** Built 100% on the **Python Standard Library** (`collections`, `argparse`, `typing`).
* 📁 **Flexible CLI Interface:** Supports direct positional arguments, ciphertext file inputs (`-f / --file`), or unattended execution (`--auto`).

---

## 🧮 Cryptographic Foundation

In Spanish texts of sufficient length, natural letter frequencies follow a well-defined non-uniform distribution:

| Character | Relative Freq (%) | Character | Relative Freq (%) |
| :---: | :---: | :---: | :---: |
| **E** | 16.78% | **D** | 6.87% |
| **A** | 11.96% | **R** | 4.94% |
| **O** | 8.69% | **U** | 4.80% |
| **L** | 8.37% | **I** | 4.15% |
| **S** | 7.88% | **T** | 3.31% |
| **N** | 7.01% | **C** | 2.92% |

The engine scans the ciphertext, calculates frequency percentages, and initializes substitution hypotheses by mapping top observed cipher symbols to top natural language letters.

---

## ⚙️ Installation & Quickstart

### 1. Clone the repository
```bash
git clone https://github.com/aimarlarriba/frequency-analysis-cipher-cli.git
cd frequency-analysis-cipher-cli
```

### 2. Execution Modes

#### A) Interactive Assisted Mode (Recommended)
Analyze a ciphertext file with the interactive REPL assistant:
```bash
python descifrar.py -f samples/cifrado_quijote.txt
```

#### B) Direct Argument Mode
```bash
python descifrar.py "Kk ec vemxo tk vx Bxkpjx..."
```

#### C) Automated Batch Mode (`--auto`)
For scripts, pipes, or unattended evaluation:
```bash
python descifrar.py -f samples/cifrado_quijote.txt --auto
```

---

## 🖥️ Interactive Console Demonstration

```text
======================================================
Cipher     Obs Freq (%)   Substitution   Ref Spanish (%)
------------------------------------------------------
x          14.85          e              16.78          
k          11.22          a              11.96          
r          9.15           o              8.69           
...
======================================================

--- PROVISIONAL DECRYPTED TEXT ---
En un lugar de la Mancha, de cuyo nombre no quiero acordarme...

Is the decrypted text legible and correct? (y/n): n

Enter manual adjustments (e.g., 'x=e' or multiple 'x=e z=a').
> x=e k=a
```

---

## 🧪 Automated Testing

Unit test suite validating frequency calculation, case preservation, and manual constraint enforcement:
```bash
python -m unittest discover tests
```

---

## 👥 Academic Context & Attribution

Originally conceptualized as an assignment for the **Security and Information Systems Security Management (SGSSI)** course at the **University of the Basque Country (UPV/EHU)**.

Refactored, modularized, and maintained by **[Aimar Larriba](https://github.com/aimarlarriba)** as an educational classical cryptanalysis utility.

---

## ⚖️ License

Distributed under the **MIT** License. See [LICENSE](LICENSE) for more details.
