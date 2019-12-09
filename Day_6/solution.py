orbits =[]
with open('day_6_input.txt','rt',encoding='utf-8') as file:
    orbits = file.readlines()

orbits = [item.replace('\n','') for item in orbits]

#orbits = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L']
planetary_groups = []
left = set()
right = set()
planet_set = set()
for orbit in orbits:
    planets = orbit.split(')')
    planetary_groups.append(planets)
    left.add(planets[0]) # orbitee
    right.add(planets[1]) # orbiter
    planet_set.add(planets[0])
    planet_set.add(planets[1])

endpoints = right.difference(left) # planets that are not orbited by other planets
# print(endpoints)
print(planetary_groups)
#print( planet_set)

orbital_map = {} # dictionary

for planet in planet_set:
    orbital_map[planet] = '' # initialize the orbit, initially empty

def orbit_builder(planet,planetary_groups,orbital_map):
    ''' Build planetary orbits for a given planet based on the complete planet set and planetary groups.
    Builds a dictionary of planets and their orbits. {'planet1': [A,B,C]} '''

    # iterate through the orbit groups, adding to the orbit if planet orbits another planet
    # i.e. if [A,planet] if A is in position 0 and planet in position 1, planet orbits A
    for group in planetary_groups:
        if(planet == group[1]): # planet is in position 1, it orbits planet in position 0
            if(group[0] not in orbital_map[planet]):
                orbital_map[planet] = group[0] # now we must recurse and use planet[0] as the orbiting planet
                orbit_builder(group[0],planetary_groups,orbital_map)
    

for planet in planet_set:
    orbit_builder(planet,planetary_groups,orbital_map)

# print(orbital_map)

orbital_paths = []

for planet in planet_set:
    planet_path = [planet]
    temp = planet
    while(True): # COM: '', COM is the end point for all planet paths
        planet_path.append(orbital_map[temp])
        if(orbital_map[temp] != ''):
            temp = orbital_map[temp] # orbital_map[temp] returns a list of 1 or empty
        else: # if orbital_map[temp] returns an empty list, break from loop
            break
    planet_path.remove('')
    orbital_paths.append(planet_path)

print(orbital_paths)

total_orbits = 0
for orbit in orbital_paths:
    total_orbits += len(orbit) -1

print(f"Total number of orbits: {total_orbits}")