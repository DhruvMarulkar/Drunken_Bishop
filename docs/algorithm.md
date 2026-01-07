# Drunken Bishop Algorithm

The Drunken Bishop algorithm is a visualization technique used by OpenSSH
to display cryptographic key fingerprints in a human-friendly way.

Instead of showing a long hexadecimal hash, the algorithm converts a
cryptographic hash into a deterministic random walk on a grid.

---

## How It Works

1. **Input Text**
   - Any string provided by the user.

2. **Hashing**
   - The input is hashed using SHA-256.
   - This ensures determinism and strong avalanche properties.

3. **Bit Pair Encoding**
   - The hash is converted into a binary string.
   - Each pair of bits controls one movement.

4. **Movement Rules**
   - `00` → up-left
   - `01` → up-right
   - `10` → down-left
   - `11` → down-right

5. **Random Walk**
   - The walk starts at the center of the grid.
   - Each step increments the visit count of the cell.

6. **Rendering**
   - Cells are rendered using increasing intensity symbols.
   - Start (`S`) and End (`E`) positions are marked.

---

## Why This Matters

- Same input always produces the same fingerprint.
- Small input changes produce visually different patterns.
- Humans can visually detect mismatches more easily than raw hashes.

This makes Drunken Bishop a useful tool for fingerprint verification.
