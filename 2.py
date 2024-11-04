# TODO Найдите количество книг, которое можно разместить на дискете
information = 1.44
book_pages = 100
number_of_lines = 50
number_of_symbol = 25
symbol = 4

byte_information = information * 1024 ** 2
V = book_pages * number_of_lines * number_of_symbol * symbol
final = byte_information // V
print("Количество книг, помещающихся на дискету:", final)