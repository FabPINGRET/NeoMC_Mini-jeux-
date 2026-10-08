# Paie $zc points (acheteur : mg.zbuyer) ; échoue si pas assez
scoreboard players operation $zh mg.st = @a[tag=mg.zbuyer,limit=1] mg.zpt
execute if score $zh mg.st < $zc mg.st run tellraw @a[tag=mg.zbuyer] [{"text":"Pas assez de points (","color":"red"},{"score":{"name":"$zc","objective":"mg.st"},"color":"yellow"},{"text":" requis).","color":"red"}]
execute if score $zh mg.st < $zc mg.st as @a[tag=mg.zbuyer] at @s run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 1 0.6
execute if score $zh mg.st < $zc mg.st run return fail
scoreboard players operation @a[tag=mg.zbuyer] mg.zpt -= $zc mg.st
execute as @a[tag=mg.zbuyer] at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 1 0.8
return 1
