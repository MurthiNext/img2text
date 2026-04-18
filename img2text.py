from colorblocks import image_to_color_blocks
from braille import image_to_braille
from asciichr import image_to_asciichr

if __name__ == "__main__":
    img_path = '1.png'
    width = 50

    ascii_result = image_to_asciichr(
        image_path=img_path,
        output_width=width
    )
    braille_result = image_to_braille(
        image_path=img_path,
        output_width=width
    )
    color_blocks_result = image_to_color_blocks(
        image_path=img_path,
        output_width=width
    )
    for a, b, c in zip(ascii_result, braille_result, color_blocks_result):
        print(a + "   " + b + "   " + c)
    with open('a.txt', 'w', encoding='utf-8') as a:
        a.write('\n'.join(ascii_result))
    with open('b.txt', 'w', encoding='utf-8') as b:
        b.write('\n'.join(braille_result))
    with open('c.txt', 'w', encoding='utf-8') as c:
        c.write('\n'.join(color_blocks_result))