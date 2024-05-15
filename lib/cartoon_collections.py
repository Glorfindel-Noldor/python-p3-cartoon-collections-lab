def roll_call_dwarves(arg):
    for int, i in enumerate(arg, start=1):
        print(f"{int}. {i}")

def summon_captain_planet(arg):
    result = []
    for word in arg:
        result.append(word.capitalize() + '!')
    return result


def long_planeteer_calls(arg):
    for i in arg:
        if len(i) > 4:
            return True
    return False


def find_the_cheese(arg):
    cheeses = ["cheddar", "gouda", "camembert"]
    for item in arg:
        if item in cheeses:
            return item
    return None
