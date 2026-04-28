import os
import click
from colorblocks import image_to_color_blocks
from braille import image_to_braille
from asciichr import image_to_asciichr

@click.command()
@click.argument('image_path', type=click.Path(exists=True))
@click.option('-w', '--width', default=50, type=int, help='输出宽度（字符数）')
@click.option('-a', '--alpha_threshold', default=128, type=int, help='Alpha 通道阈值，低于此值视为透明 (0-255)')
@click.option('-c', '--colored', is_flag=True, default=False, help='启用 ANSI 颜色代码输出')
@click.option('-m', '--mode', type=click.Choice(['a', 'b', 'c'], case_sensitive=False), help='输出模式：a=ASCII, b=盲文, c=半色块')
@click.option('-o', '--output', type=str, help='输出文件名')
def main(image_path, width, alpha_threshold, colored, mode, output):
    """
    将图片转换为三种风格的彩色字符画（ASCII、盲文、半色块）。
    透明区域自动替换为空格。
    """
    mode_funcs = {
        'a': image_to_asciichr,
        'b': image_to_braille,
        'c': image_to_color_blocks,
    }
    mode_names = {
        'a': 'ASCII',
        'b': '盲文',
        'c': '半色块',
    }
    mode_defaults = {
        'a': 'a.txt',
        'b': 'b.txt',
        'c': 'c.txt',
    }

    if mode:
        mode = mode.lower()
        modes_to_run = [mode]
    else:
        modes_to_run = ['a', 'b', 'c']

    results = {}
    for m in modes_to_run:
        results[m] = mode_funcs[m](
            image_path=image_path,
            output_width=width,
            alpha_threshold=alpha_threshold,
            colored=colored
        )

    # 终端显示
    if len(modes_to_run) == 3:
        for a_line, b_line, c_line in zip(results['a'], results['b'], results['c']):
            print(a_line + "   " + b_line + "   " + c_line)
    else:
        for line in results[modes_to_run[0]]:
            print(line)

    # 保存到文件
    for m in modes_to_run:
        if output:
            if mode:
                filename = output
            else:
                base, ext = os.path.splitext(output)
                filename = f"{base}_{m}{ext}"
        else:
            filename = mode_defaults[m]

        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(results[m]))
        print(f"已保存 {mode_names[m]} 结果到 {filename}")

if __name__ == '__main__':
    main()