def create_character(name, strength, intelligence, charisma):
    # Validate character name
    if type(name) is not str:
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
        
    # Validate stat types (using type() to strictly avoid booleans passing as ints)
    if type(strength) is not int or type(intelligence) is not int or type(charisma) is not int:
        return "All stats should be integers"
        
    # Validate stat minimums
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
        
    # Validate stat maximums
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
        
    # Validate stat sum
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"
        
    # Generate the dots for each stat
    full_dot = '●'
    empty_dot = '○'
    
    s = (full_dot * strength) + (empty_dot * (10 - strength))
    i = (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    c = (full_dot * charisma) + (empty_dot * (10 - charisma))
    
    # Return the final formatted string
    return f'{name}\nSTR {s}\nINT {i}\nCHA {c}'

create_character("Aragorn", 3, 2, 2)