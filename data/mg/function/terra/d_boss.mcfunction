# Carnotaure de défense (ici)
function mg:terra/dino/carno
scoreboard players set $tvcc mg.st 240
execute as @e[tag=mg.tvlast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure,distance=..60]
tellraw @a[tag=mg.tvw,distance=..80] {"text":"🦖 Un carnotaure fonce sur l'outpost !","color":"red","bold":true}
execute as @a[tag=mg.tvw,distance=..80] at @s run playsound minecraft:entity.ravager.roar hostile @s ~ ~ ~ 1 0.55
