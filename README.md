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

📢 Acknowledgement
Thanks to my friend @syswraith for introducing me to the concept of the Drunken Bishop algorithm.
