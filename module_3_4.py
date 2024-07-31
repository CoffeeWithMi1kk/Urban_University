# Задание №1
def single_root_words(root_word, *other_words):
    root_word_lower = root_word.lower()
    # Задание №2
    same_words = []

    # Задание №3
    for word in other_words:
        word_lower = word.lower()
        # Задание №4
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    # Задание №5
    return same_words

# Задание №6
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
