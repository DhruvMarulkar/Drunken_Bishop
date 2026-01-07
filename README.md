# 🧭 Drunken Bishop Fingerprint Visualizer

A Python CLI tool inspired by OpenSSH’s **Drunken Bishop algorithm** that converts text into
**cryptographic fingerprints** using a deterministic random-walk visualization.

The project supports **ASCII fingerprints**, **PNG image output**, and a **compare mode**
to demonstrate the **avalanche effect** in cryptographic hashing.

---

## ✨ Features

- Deterministic fingerprint generation using **SHA-256**
- ASCII art visualization in the terminal
- PNG image (heatmap-style) output
- Compare mode to visualize small input changes
- Clean CLI interface
- Modular Python package with tests
- Installable as a CLI tool

---

## 🧠 How It Works

1. **Hashing**  
   The input text is hashed using **SHA-256**, ensuring deterministic behavior.

2. **Bit Pair Encoding**  
   The hash is converted into a binary stream.  
   Every 2 bits define a diagonal move:
   - `00` → up-left  
   - `01` → up-right  
   - `10` → down-left  
   - `11` → down-right  

3. **Drunken Walk**  
   Starting from the grid center, the “bishop” walks according to these moves while
   recording visit counts per cell.

4. **Rendering**  
   - ASCII symbols represent visit intensity
   - PNG images visualize the same grid as a heatmap
   - Start (`S`) and End (`E`) positions are highlighted

---

## 🚀 Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd Drunken_Bishop
Install dependencies:

bash
Copy code
pip install pillow
(Optional) Install as a CLI tool:

bash
Copy code
pip install -e .
▶️ Usage
Run from the project root or after installation.

Single input (ASCII output)
bash
Copy code
drunken-bishop hello
Save ASCII output to file
bash
Copy code
drunken-bishop hello --output examples/hello.txt
Generate PNG image
bash
Copy code
drunken-bishop hello --image examples/hello.png
Compare two inputs (avalanche effect)
bash
Copy code
drunken-bishop hello "hello!"
Compare + PNG output
bash
Copy code
drunken-bishop hello "hello!" --image examples/compare.png
🖼️ Example Outputs
Example ASCII and PNG fingerprints are available in the examples/ directory.
Small changes in input result in visually different patterns.

🧪 Tests
Run tests from the project root:

bash
Copy code
pytest
Tests verify:

Deterministic behavior

Avalanche effect

Non-empty fingerprint generation

📂 Project Structure
markdown
Copy code
Drunken_Bishop/
├── drunken_bishop/
│   ├── __init__.py
│   ├── core.py
│   └── __main__.py
├── tests/
├── examples/
├── docs/
├── pyproject.toml
├── README.md
└── .gitignore

📢 Acknowledgement
Thanks to my friend @syswraith for introducing me to the concept of the Drunken Bishop algorithm.