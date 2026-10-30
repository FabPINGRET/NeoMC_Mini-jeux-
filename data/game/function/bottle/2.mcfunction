give @s minecraft:glass_bottle
playsound minecraft:zelda.itemget master @s ~ ~ ~ 1 1
tag @s add bottle2

execute as @s if entity @s[tag=bottle1,tag=bottle2,tag=bottle3] run advancement grant @s only sidequest_2:bottles
execute as @a[tag=mg.flw] run function game:100_check
