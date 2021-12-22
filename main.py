import string

# перечиляем поддерживаемые кодировки
codecs = ["cp1252", "cp437", "utf-16be", "utf-16","utf8"]

hello="работаем со строками"
print(hello)

# пробуем работать в branch unt8
stringutf8 = "string " + codecs[4] + " add"
print(stringutf8)