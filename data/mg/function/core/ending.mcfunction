# Fin de partie / célébration (état 3)
scoreboard players remove $timer mg.st 1

# Confettis sur le(s) vainqueur(s)
execute if score $timer mg.st matches 5.. at @a[tag=mg.win] run particle minecraft:totem_of_undying ~ ~1 ~ 0.4 0.7 0.4 0.3 30
execute if score $timer mg.st matches 100 as @a at @s run playsound minecraft:entity.firework_rocket.launch master @s ~ ~ ~ 1 1
execute if score $timer mg.st matches 80 as @a at @s run playsound minecraft:entity.firework_rocket.blast master @s ~ ~ ~ 1 1
execute if score $timer mg.st matches 60 as @a at @s run playsound minecraft:entity.firework_rocket.large_blast master @s ~ ~ ~ 1 0.9
execute if score $timer mg.st matches 40 as @a at @s run playsound minecraft:entity.firework_rocket.twinkle master @s ~ ~ ~ 1 1

execute if score $timer mg.st matches ..0 run function mg:core/return_lobby
