# Manche terminée
execute if score $zr mg.st matches 10.. run return run function mg:zm3/victory
scoreboard players set $zph mg.st 0
scoreboard players set $zb mg.st 200
tellraw @a[tag=mg.play] [{"text":"🧟 Manche ","color":"dark_green"},{"score":{"name":"$zr","objective":"mg.st"},"color":"green","bold":true},{"text":" terminée ! Prochaine dans 10 s.","color":"gray"}]
execute as @a[tag=mg.play,tag=mg.zdead] run function mg:zm3/revive
execute as @a[tag=mg.play] at @s run playsound minecraft:block.bell.use master @s ~ ~ ~ 1 0.8
