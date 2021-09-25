def emoji_converter(characters):
    words = characters.split(' ')

    emoji = {
        ':)': '😊',
        ':(': '😢',
        'XD': '🤣',
        '<3': '😍'
    }

    output = ""
    for items in words:
        output += emoji.get(items, items) + " "
    return output


characters = input(">")
print(emoji_converter(characters))
