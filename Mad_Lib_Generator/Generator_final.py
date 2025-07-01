import random

user_name = input("Enter a name: ")
user_place = input("Enter a place: ")
user_noun = input("Enter a noun: ")
user_verb = input("Enter a verb: ")
user_adjective = input("Enter an adjective: ")
user_adverb = input("Enter an adverb: ")

word_map = {
    "name": user_name,
    "place": user_place,
    "noun": user_noun,
    "verb": user_verb,
    "adjective": user_adjective,
    "adverb": user_adverb
}

templates = [
    "One day, {name} went to the {place}. They saw a {adjective} {noun} trying to {verb} {adverb}.",
    "At the {place}, {name} discovered a {noun} that loved to {verb} {adverb}. It was so {adjective}!",
    "{name} had always dreamed of visiting the {place}, where {noun}s {verb} {adverb} all day. It was a {adjective} sight.",
    "Nobody believed {name} until they went to the {place} and saw a {adjective} {noun} {verb} {adverb}.",
    "When {name} visited the {place}, a {adjective} {noun} tried to {verb} {adverb}. What an adventure!",
    "Deep inside the {place}, {name} encountered a {adjective} {noun} that could {verb} {adverb}.",
    "{name} looked at the {noun} in the {place} and said, 'How {adjective} you {verb} so {adverb}!'",
    "In a strange land called {place}, {name} found a {adjective} {noun} who liked to {verb} {adverb}.",
    "{name} opened a secret door in the {place} and saw a {adjective} {noun} {verb} {adverb}.",
    "The legend says {name} once made a {adjective} {noun} {verb} {adverb} in the {place}.",
    "Back in the {place}, {name} built a {adjective} {noun} to {verb} {adverb}.",
    "{name} heard a noise in the {place}. It was a {adjective} {noun} trying to {verb} {adverb}.",
    "Inside the mysterious {place}, {name} met a {adjective} {noun} who would {verb} {adverb}.",
    "Long ago in the {place}, {name} and a {noun} had to {verb} {adverb} to escape a {adjective} trap.",
    "While hiking through the {place}, {name} tripped over a {adjective} {noun} trying to {verb} {adverb}.",
    "No one expected {name} to {verb} a {adjective} {noun} {adverb} at the {place}.",
    "During the trip to the {place}, {name} made a {adjective} friend: a {noun} who {verb} {adverb}.",
    "In {place}, {name} saw clouds shaped like {noun}s {verb}ing {adverb}. It felt so {adjective}!",
    "The {place} was haunted by a {adjective} {noun} that {name} had to {verb} {adverb}.",
    "{name} and their {noun} walked into the {place} and began to {verb} {adverb}. It was {adjective}.",
    "{name} took their {adjective} {noun} to the {place} so it could {verb} {adverb}.",
    "In a dream, {name} flew to the {place} and found a {noun} {verb}ing {adverb}. It was very {adjective}.",
    "At midnight in the {place}, {name} was startled by a {adjective} {noun} trying to {verb} {adverb}.",
    "Every {place} has its secrets, but {name} never expected to find a {adjective} {noun} {verb}ing {adverb}.",
    "With a map in hand, {name} journeyed to the {place} in search of a {adjective} {noun} that could {verb} {adverb}."
]

story_number = 1
while True:
    print(f"\nStory {story_number}:")
    template = random.choice(templates)
    story = template.format(**word_map)
    print(story)

    choice = input("\nEnter 0 to stop or any other key to continue: ")
    if choice == "0":
        print("\nThanks for playing Mad Libs!")
        break

    story_number += 1
