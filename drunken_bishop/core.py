import time
import hashlib
import argparse

SYMBOLS = [' ', '.', 'o', '+', '=', '*', 'B', '0', 'X', '@', '%', '&', '#', '/', '^']


def hash_to_bits(text: str) -> str:
    """Convert input text into SHA-256 bit string."""
    hash_bytes = hashlib.sha256(text.encode("utf-8")).digest()
    return "".join(f"{b:08b}" for b in hash_bytes)


def generate_walk(bits, width, height):
    """Generate drunken bishop walk grid."""
    moves = {
        "00": (-1, -1),
        "01": (1, -1),
        "10": (-1, 1),
        "11": (1, 1)
    }

    grid = [[0 for _ in range(width)] for _ in range(height)]

    x = width // 2
    y = height // 2
    start = (x, y)

    for i in range(0, len(bits), 2):
        step = bits[i:i + 2]
        if len(step) < 2:
            break

        dx, dy = moves[step]
        x = max(0, min(width - 1, x + dx))
        y = max(0, min(height - 1, y + dy))
        grid[y][x] += 1

    end = (x, y)
    return grid, start, end


def render_grid(grid, start, end):
    height = len(grid)
    width = len(grid[0])
    max_visits = len(SYMBOLS) - 1

    lines = []
    border = "+" + "-" * width + "+"
    lines.append(border)

    for r in range(height):
        line = "|"
        for c in range(width):
            if (c, r) == start:
                line += "S"
            elif (c, r) == end:
                line += "E"
            else:
                val = grid[r][c]
                line += SYMBOLS[min(val, max_visits)]
        line += "|"
        lines.append(line)

    lines.append(border)
    return "\n".join(lines)

from PIL import Image


def render_image(grid, start, end, cell_size=20):
    """
    Render the fingerprint grid as a PNG image.
    """
    height = len(grid)
    width = len(grid[0])
    max_val = max(max(row) for row in grid) or 1

    img = Image.new("RGB", (width * cell_size, height * cell_size), "white")
    pixels = img.load()

    for y in range(height):
        for x in range(width):
            val = grid[y][x]

            
            intensity = int(255 * (val / max_val))
            color = (255 - intensity, 255 - intensity, 255)

            # start/end markers
            if (x, y) == start:
                color = (0, 200, 0)     
            elif (x, y) == end:
                color = (200, 0, 0)      

            for i in range(cell_size):
                for j in range(cell_size):
                    pixels[x * cell_size + i, y * cell_size + j] = color

    return img


def drunken_bishop(text, width=17, height=9, animate=False, delay=0.05):
    bits = hash_to_bits(text)
    grid = [[0 for _ in range(width)] for _ in range(height)]

    moves = {
        "00": (-1, -1),
        "01": (1, -1),
        "10": (-1, 1),
        "11": (1, 1)
    }

    x = width // 2
    y = height // 2
    start = (x, y)

    for i in range(0, len(bits), 2):
        step = bits[i:i + 2]
        if len(step) < 2:
            break

        dx, dy = moves[step]
        x = max(0, min(width - 1, x + dx))
        y = max(0, min(height - 1, y + dy))
        grid[y][x] += 1

        if animate:
            print("\033c", end="")
            print(f"Step {i // 2 + 1}/{len(bits) // 2}")
            print(render_grid(grid, start, (x, y)))
            time.sleep(delay)

    fingerprint = render_grid(grid, start, (x, y))
    print("Final Fingerprint:")
    print(fingerprint)

    return fingerprint, grid, start, (x, y)
    
def parse_args():
    parser = argparse.ArgumentParser(
        description="Drunken Bishop fingerprint visualization tool"
    )

   
    parser.add_argument(
        "texts",
        nargs="+",
        help="One or two input strings"
    )

    parser.add_argument(
        "--width",
        type=int,
        default=17,
        help="Grid width (default: 17)"
    )

    parser.add_argument(
        "--height",
        type=int,
        default=9,
        help="Grid height (default: 9)"
    )

    parser.add_argument(
        "--animate",
        action="store_true",
        help="Animate the random walk"
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=0.05,
        help="Animation delay in seconds"
    )

    parser.add_argument(
        "--output",
        type=str,
        help="Save fingerprint output to a file"
    )

    parser.add_argument(
        "--image",
        type=str,
        help="Save fingerprint as PNG image"
    )

    return parser.parse_args()

def main():
    args = parse_args()

    if len(args.texts) > 2:
        print("Error: Provide at most two inputs.")
        return

    outputs = []

    for idx, text in enumerate(args.texts, start=1):
        print(f"\nINPUT {idx}: {text}")
        fingerprint, grid, start, end = drunken_bishop(
              text,
              width=args.width,
              height=args.height,
              animate=args.animate,
              delay=args.delay
        )

        outputs.append(f"INPUT {idx}: {text}\n{fingerprint}")

    if args.image:
      img = render_image(grid, start, end)
      img.save(args.image)
      print(f"Image saved to {args.image}")

