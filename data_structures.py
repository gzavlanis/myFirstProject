# Lists
famous_people = ["Albert Einstein", "William Shakespeare", "Marie Curie", "Isaac Newton", "Ada Lovelace"]
first_person = famous_people[0]
third_person = famous_people[2]
print(famous_people[-1])
print("George Zavlanis" in famous_people)

print(first_person)
print(third_person)

famous_people[1] = "William Shakespeare Jr."
print(famous_people)

famous_people.append("Charles Darwin")
famous_people.insert(2, "Galileo Galilei")
famous_people.remove("Marie Curie")
last_person = famous_people.pop()

print(famous_people)
print(last_person)

top_three_people = famous_people[0:3]
print(top_three_people)

# tuples
fruits = ("Apple", "Banana", "Cherry")

first_fruit = fruits[0]
print(first_fruit)

new_fruit = ("Orange",)
updated_fruits = fruits + new_fruit
print(updated_fruits)

fruit_quantities = (5, 3, 2, 5, 1, 4, 5)
fruit_name = "Apple"
fruit_count = fruit_quantities.count(5)
fruit_position = fruits.index(fruit_name)

print(f"We have {fruit_count} {fruit_name}s, which is the first fruit in our list (position {fruit_position}).")

# Sets
beautiful_flowers = {"Rose", "Lily", "Tulip", "Daisy"}
print(beautiful_flowers)

beautiful_flowers.add("Sunflower")
print(beautiful_flowers)

beautiful_flowers.remove("Tulip")
print(beautiful_flowers)

flower_bouquet_a = {"Rose", "Lily", "Tulip"}
flower_bouquet_b = {"Tulip", "Daisy", "Sunflower"}

# Union
all_flowers = flower_bouquet_a.union(flower_bouquet_b)
print("Union:", all_flowers)

# Intersection
common_flowers = flower_bouquet_a.intersection(flower_bouquet_b)
print("Intersection:", common_flowers)

# Difference
unique_flowers = flower_bouquet_a.difference(flower_bouquet_b)
print("Difference:", unique_flowers)

# Dictionaries
spellbook = {
    "Lumos": "Creates light",
    "Expelliarmus": "Disarms opponent",
    "Wingardium Leviosa": "Levitates objects"
}

lumos_effect = spellbook["Lumos"]
print(lumos_effect)

spellbook["Expelliarmus"] = "Disarms opponent and dislodges objects"
print(spellbook)

del spellbook["Wingardium Leviosa"]
print(spellbook)

spells = spellbook.keys()
print(spells)

spell_effects = spellbook.values()
print(spell_effects)

spellbook_items = spellbook.items()
print(spellbook_items)

effect = spellbook.get('Alohomora', 'Spell not found in the spellbook.')
print(effect)

additional_spells = {
    'Alohomora': 'Unlocks doors',
    'Avada Kedavra': 'Causes instant death'
}

spellbook.update(additional_spells)
print(spellbook)

spellbook.clear()
print(spellbook)

print(len(set([1, 2, 2, 3, 3, 3])))

positions = {1: 'Striker', 2: 'Midfielder', 3: 'Defender'}
print(positions.get(4, 'Goalkeeper'))