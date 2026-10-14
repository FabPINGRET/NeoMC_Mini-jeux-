scoreboard players set $tvf mg.st 1
scoreboard players set $tvcc mg.st 240
function mg:terra/dino/carno
tellraw @a[tag=mg.tvw] {"text":"🦖 Un rugissement résonne dans la jungle… un carnotaure rôde.","color":"red"}
execute as @a[tag=mg.tvw] at @s run playsound minecraft:entity.ravager.roar hostile @s ~ ~ ~ 0.6 0.55
