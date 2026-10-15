# Chute <-> accalmie, avec une nouvelle durée tirée au hasard (absent : 1, ça tombe)
execute store success score $thw mg.st unless score $thw mg.st matches 1
execute if score $thw mg.st matches 1 store result score $thd mg.st run random value 60..240
execute if score $thw mg.st matches 0 store result score $thd mg.st run random value 60..180
