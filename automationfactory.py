def sort(width, height, length, mass):

    #Calculate volume and check if bulky
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or any(dim >= 150 for dim in [width, height, length])
    
    #Check if heavy
    is_heavy = mass >= 20

    #Dispatch based on criteria
    if is_bulky and is_heavy:
        return "REJECTED"
    
    if is_bulky or is_heavy:
        return "SPECIAL"
    
    return "STANDARD"




print(sort(20, 10, 50, 10))