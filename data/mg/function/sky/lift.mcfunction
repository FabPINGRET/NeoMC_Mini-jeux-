# Entrée dans une colonne de vent (@s) : 1,5 s de lévitation, puis 5 s avant la suivante
scoreboard players set @s mg.skl 130
effect give @s minecraft:levitation infinite 9 true
playsound minecraft:entity.breeze.wind_burst master @s ~ ~ ~ 1 1
