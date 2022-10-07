s = "azcbobobegghakl"
vowels = "aeiou"

total_bobs = s.count("bob")
total = [letter for letter in s if letter in vowels]
print(total_bobs)
