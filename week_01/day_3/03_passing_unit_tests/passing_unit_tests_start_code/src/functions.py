def greet_catalan(name):
    return f"Hola, {name}"


def find_chicken_by_name(chickens, name):
    found_chicken = None

    for chicken in chickens:
        if chicken["name"] == name:
            found_chicken = chicken
            break

    return found_chicken