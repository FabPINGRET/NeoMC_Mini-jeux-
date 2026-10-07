# Bruit du moteur de @s selon sa vitesse (entendu par lui et les pilotes proches)
execute if score @s mg.ksp matches 1..29 at @s run playsound minecraft:block.note_block.didgeridoo player @a[tag=mg.play,distance=..12] ~ ~ ~ 0.14 0.55
execute if score @s mg.ksp matches 30..59 at @s run playsound minecraft:block.note_block.didgeridoo player @a[tag=mg.play,distance=..12] ~ ~ ~ 0.14 0.65
execute if score @s mg.ksp matches 60..89 at @s run playsound minecraft:block.note_block.didgeridoo player @a[tag=mg.play,distance=..12] ~ ~ ~ 0.14 0.78
execute if score @s mg.ksp matches 90..109 at @s run playsound minecraft:block.note_block.didgeridoo player @a[tag=mg.play,distance=..12] ~ ~ ~ 0.14 0.9
execute if score @s mg.ksp matches 110..139 at @s run playsound minecraft:block.note_block.didgeridoo player @a[tag=mg.play,distance=..12] ~ ~ ~ 0.14 1.05
execute if score @s mg.ksp matches 140..999 at @s run playsound minecraft:block.note_block.didgeridoo player @a[tag=mg.play,distance=..12] ~ ~ ~ 0.14 1.25
execute if score @s mg.kdr matches 1.. at @s run playsound minecraft:block.gravel.step player @a[tag=mg.play,distance=..12] ~ ~ ~ 0.5 1.4
