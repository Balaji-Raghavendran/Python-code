input_value = input("Enter a sentence: ")
vowels = "aeiou"                         
sentence = input_value.lower()           #converting the stored values into lowercase
for vowel in vowels:
    count_vowel = sentence.count(vowel)        #counts each vowels and stores inside count_vowel variable
    print(f"{vowel.upper()} - {count_vowel}")  #displays the vowels as uppercase and vowels count appeared in the sentence.