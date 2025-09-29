 # Mars exploration program
print("Welcome to Mars exploration!")

def explore_mars():
    """Function to simulate Mars exploration"""
    locations = ["Olympus Mons", "Valles Marineris", "Polar Ice Caps", "Gale Crater"]
    
    print("Exploring Mars locations:")
    for location in locations:
        print(f"- Visiting {location}")
    
    return "Mars exploration complete!"

def mars_facts():
    """Display interesting facts about Mars"""
    facts = [
        "Mars is the fourth planet from the Sun",
        "Mars has two small moons: Phobos and Deimos", 
        "A day on Mars is about 24 hours and 37 minutes",
        "Mars has the largest volcano in the solar system"
    ]
    
    print("\nMars Facts:")
    for fact in facts:
        print(f"• {fact}")

if __name__ == "__main__":
    result = explore_mars()
    mars_facts()
    print(f"\nStatus: {result}")