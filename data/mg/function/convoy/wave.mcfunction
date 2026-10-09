# Vague : 1 + nombre de joueurs monstres (max 8), devant le convoi ; 30 au plus en même temps
scoreboard players set $cvw mg.st 0
execute store result score $cvk mg.st if entity @e[tag=mg.cvm]
execute if score $cvk mg.st matches 30.. run return 0
execute store result score $cvk mg.st if entity @a[tag=mg.play]
scoreboard players add $cvk mg.st 1
execute if score $cvk mg.st matches 9.. run scoreboard players set $cvk mg.st 8
execute if score $cvp mg.st matches 101.. run scoreboard players set $cvk mg.st 0
execute at @e[type=minecraft:block_display,tag=mg.cvc,limit=1] positioned ~20 81 21200.5 run function mg:convoy/wave_one
