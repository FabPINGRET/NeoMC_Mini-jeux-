# Parkour du lobby — tick (appelé à chaque tick)
scoreboard players set $pk20 mg.st 20
scoreboard players set $pk2 mg.st 2
# Pendant une partie : plus de course
execute unless score $state mg.st matches 0 run tag @a remove mg.pkr
execute as @a[tag=mg.pkr,gamemode=!adventure] run tag @s remove mg.pkr
# Plot de départ : (re)lance une course
execute if score $state mg.st matches 0 as @a[tag=mg.init,tag=!mg.play,tag=!mg.out,gamemode=adventure] at @s if entity @e[type=minecraft:marker,tag=mg.pks,distance=..2.3] run function mg:parkour/start
# Coureurs
execute as @a[tag=mg.pkr] at @s run function mg:parkour/run
