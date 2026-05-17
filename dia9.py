import unicodedata

def remove_accents(phrase):
    return unicodedata.normalize('NFKD', phrase).encode('ascii', 'ignore').decode('ascii')

def analyze_phrase(phrase):
    total_characters = len(phrase)
    spaces = phrase.count(' ')
    vowels = sum(1 for char in phrase if char.lower() in 'aeiou')
    consonants = sum(1 for char in phrase if char.isalpha() and char.lower() not in 'aeiou')
    
    return total_characters, spaces, vowels, consonants

def is_palindrome(phrase):
    cleaned_phrase = remove_accents(phrase)
    cleaned_phrase = ''.join(char.lower() for char in cleaned_phrase if char.isalnum())
    return cleaned_phrase == cleaned_phrase[::-1]

def reverse_phrase(phrase):
    return phrase[::-1]

user_phrase = input("Introduce una frase:\n")
total_characters, spaces, vowels, consonants = analyze_phrase(user_phrase)
print(f"\nCaracteres: {total_characters}")
print(f"Espacios: {spaces}")
print(f"Vocales: {vowels}")
print(f"Consonantes: {consonants}")
print(f"Palíndromo: {is_palindrome(user_phrase)}")
print(f"Frase invertida: {reverse_phrase(user_phrase)}")
