# @s touche un point de passage (mg.t du marqueur le plus proche)
execute store result score $c mg.st run scoreboard players get @e[type=minecraft:marker,tag=mg.sjc,sort=nearest,limit=1] mg.t
execute unless score $c mg.st > @s mg.sjp run return 0
scoreboard players operation @s mg.sjp = $c mg.st
execute at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.6
tellraw @a[tag=mg.play] [{"text":"✔ ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" passe le point ","color":"gray"},{"score":{"name":"$c","objective":"mg.st"},"color":"green","bold":true},{"text":"/4","color":"green"}]
