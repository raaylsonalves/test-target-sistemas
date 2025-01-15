def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

string = input("Informe uma palavra: ")
string_invertida = reverse_string(string)
print("String original:", string)
print("String invertida:", string_invertida)
