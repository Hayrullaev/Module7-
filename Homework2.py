def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings):
            file.write(string + '\n')
            start_byte = file.tell()
            strings_positions[i, start_byte] = string
    return strings_positions

info =  [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('file_name.txt', info)
for elem in result.items():
  print(elem)