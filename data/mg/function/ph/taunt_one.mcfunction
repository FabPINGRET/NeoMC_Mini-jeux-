execute store result score $phq mg.st run random value 0..3
execute if score $phq mg.st matches 0 run playsound minecraft:entity.cat.ambient player @a ~ ~ ~ 1.2 1.2
execute if score $phq mg.st matches 1 run playsound minecraft:entity.chicken.ambient player @a ~ ~ ~ 1.2 1
execute if score $phq mg.st matches 2 run playsound minecraft:entity.villager.ambient player @a ~ ~ ~ 1.2 1.3
execute if score $phq mg.st matches 3 run playsound minecraft:block.note_block.bell player @a ~ ~ ~ 1.2 1.8
particle minecraft:note ~ ~1 ~ 0.2 0.2 0.2 1 2
