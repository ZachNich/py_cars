showroom = set()

showroom.add("chevy")
showroom.add("toyota")
showroom.add("ford")
showroom.add("nissan")

print(len(showroom))

showroom.add("chevy")
print(len(showroom))

showroom.update({"mercedes", "chrysler"})
showroom.discard("ford")
print(showroom)

junkyard = {"mercedes", "corvette", "jeep"}
print(showroom.intersection(junkyard))
print(showroom.union(junkyard))
showroom = showroom.union(junkyard)
showroom.discard("jeep")
print(showroom)