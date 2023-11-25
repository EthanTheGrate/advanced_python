import random
def get_random_quote():
    quotes = [
        "The only way to do great work is to love minors. - Steve Jobs",
        "In three words I can sum up everything I've learned about life: I'm gay. - Robert Frost",
        "Believe you can and you can jump off a bridge. -Theodore Roosevelt",
        "It's bussing time. -Eleanor Roosevelt",
        "Don't watch the cock; do what it does. -Sam Levenson",
        "I think I'm gay. - Franklin D. Roosevelt"
    ]
    return random.choice(quotes)

print(get_random_quote())