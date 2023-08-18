def print_decorated_header(title):
    title_length = len(title)
    top_border = " ╔" + "═" * (title_length + 4) + "╗ "
    bottom_border = " ╚" + "═" * (title_length + 4) + "╝ "
    content = f" ║  {title}  ║ "

    print(top_border)
    print(content)
    print(bottom_border)
