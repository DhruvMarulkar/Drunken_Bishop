# Drunken Bishop Visualization

A Python implementation of the **Drunken Bishop algorithm** — a random-walk visual fingerprint generator.  
Given an input word or string, this program produces a unique ASCII art pattern representing that word’s “fingerprint.”

This algorithm is famously used for SSH key fingerprint visualization.

---

## 🔍 How It Works

1. **Convert Input to Binary**  
   The input word is encoded into UTF-8 bytes and converted to a long string of binary bits.

2. **Map Bits to Moves**  
   Every 2 bits determine one move of the “bishop” on a grid:
   - `00` → up-left
   - `01` → up-right
   - `10` → down-left
   - `11` → down-right

3. **Add Randomness**  
   Small random variations are added to each move to simulate a “drunken” walk.

4. **Track Visits**  
   Each cell in the grid records how many times it was visited.

5. **Generate ASCII Art**  
   Each visit count is mapped to a symbol. The result is a unique ASCII art fingerprint.

---

## 🎨 Symbol Mapping

| Visits | Symbol |
|--------|--------|
| 0      | ` `     |
| 1      | `.`     |
| 2      | `o`     |
| 3      | `+`     |
| 4      | `=`     |
| 5      | `*`     |
| 6      | `B`     |
| 7      | `0`     |
| 8      | `X`     |
| 9      | `@`     |
| 10     | `%`     |
| 11     | `&`     |
| 12     | `#`     |
| 13     | `/`     |
| ≥14    | `^`     |

## 📢 Acknowledgement

Thanks to my friend [@syswraith](https://syswraith.com/) for introducing me to the concept of the Drunken Bishop algorithm.
---
git clone https://github.com/yourusername/drunken-bishop.git
cd drunken-bishop
