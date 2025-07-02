import random

templates = [
    "Once upon a time in {place}, there lived a person named {name}. {name} loved to {hobby} every day with a {animal}.",
    "{name} went to {place} to learn how to {activity}. There they met a talking {animal} who changed their life.",
    "In the heart of {place}, {name} discovered a magical {object} that could grant the power of {superpower}.",
    "{name} and their best friend, a {animal}, built a rocket to travel from {place} to Mars.",
    "Long ago, in {place}, there was a secret school for people who could {superpower}. {name} was the youngest student.",
    "During a trip to {place}, {name} stumbled upon an old map leading to a hidden {object}.",
    "Every evening, {name} would sit by the {place} river and dream about {dream}.",
    "It was a rainy day in {place}, and {name} was bored. Suddenly, a {animal} knocked on the door!",
    "{name} never expected that a simple walk in {place} would lead to discovering the secret of {object}.",
    "One day, {name} woke up and realized they had turned into a {animal}! They had to find a way to get back to normal.",
    "{name} and {friend} opened a small shop in {place}, but strange things began to happen when they found a {object}.",
    "While exploring the caves of {place}, {name} found ancient writings that spoke of a {superpower}.",
    "{name}'s favorite hobby was {hobby}, but everything changed when a {animal} entered their life.",
    "{name} loved adventures. One morning, they packed a bag, left {place}, and started their quest for {object}.",
    "After touching a glowing stone in {place}, {name} could suddenly {superpower}.",
    "Once, {name} hosted a grand party in {place}, and a mischievous {animal} crashed it.",
    "Legend says a hero named {name} from {place} saved the world using a {object}.",
    "{name} was just a student in {place}, but when danger arose, they became the {superpower} hero.",
    "{name} always wanted to meet aliens. One night in {place}, they got their wish.",
    "{name} built a robot named {friend}, and together they protected {place} from danger.",
    "A magical portal opened in {place}, and {name} was pulled into a world of {superpower} creatures.",
    "As the sun set on {place}, {name} prepared for their final battle using the mighty {object}.",
]

def get_user_inputs():
    return {
        "name": input("Enter a name: "),
        "place": input("Enter a place: "),
        "animal": input("Enter an animal: "),
        "object": input("Enter an object: "),
        "hobby": input("Enter a hobby: "),
        "superpower": input("Enter a superpower: "),
        "activity": input("Enter an activity: "),
        "dream": input("Enter a dream: "),
        "friend": input("Enter a friend's name: "),
    }
inputs = get_user_inputs()
while True:
    print("\n--- STORY GENERATOR ---")
    template = random.choice(templates)
    story = template.format(**inputs)
    print("\nGenerated Story:\n" + "*" * 60)
    print(story)
    print("*" * 60)
    print("Enter '0' to stop.")
    if input("Press Enter to continue or 0 to stop: ") == '0':
        break