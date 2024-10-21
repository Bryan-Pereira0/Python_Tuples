def itinerary(itineraries):
    for i, (name, origin, destination) in enumerate(itineraries, 1):
        print(f"Itinerary {i}: {name} - From {origin} to {destination}")
        
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
itinerary(itineraries)