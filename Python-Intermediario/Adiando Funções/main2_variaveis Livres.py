def concat(string_qualquer_1):
    string_completa = string_qualquer_1

    def concatenando(string_qualquer_2):
        nonlocal string_completa
        string_completa += string_qualquer_2
        return string_completa

    return concatenando


c = concat("Ola")
print(c(" Mundo"))
print(c(" Cruel"))
