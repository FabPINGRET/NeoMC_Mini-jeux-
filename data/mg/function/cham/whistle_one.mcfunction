execute store result score $cmq mg.st run random value 0..2
execute if score $cmq mg.st matches 0 run playsound minecraft:block.note_block.flute player @a ~ ~ ~ 1.3 1.6
execute if score $cmq mg.st matches 1 run playsound minecraft:block.note_block.chime player @a ~ ~ ~ 1.3 1.2
execute if score $cmq mg.st matches 2 run playsound minecraft:entity.parrot.ambient player @a ~ ~ ~ 1.3 1.3
particle minecraft:note ~ ~1 ~ 0.2 0.2 0.2 1 3
scoreboard players add @s mg.cmpts 3
