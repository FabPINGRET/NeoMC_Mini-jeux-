# Fin des 6 trous : le plus petit total gagne (égalité = match nul)
execute unless score $state mg.st matches 2 run return 0
tellraw @a[tag=mg.play] [{"text":"⛳ Parcours terminé ! ","color":"green","bold":true},{"text":"(par 23)","color":"gray"}]
execute as @a[tag=mg.play] run tellraw @a[tag=mg.play] [{"text":"  ","color":"gray"},{"selector":"@s","color":"yellow"},{"text":" : ","color":"gray"},{"score":{"name":"@s","objective":"mg.gft"},"color":"white","bold":true},{"text":" coups","color":"gray"}]
scoreboard players set $gfmin mg.st 999
scoreboard players operation $gfmin mg.st < @a[tag=mg.play] mg.gft
scoreboard players set $gfnb mg.st 0
execute as @a[tag=mg.play] if score @s mg.gft = $gfmin mg.st run scoreboard players add $gfnb mg.st 1
execute if score $gfnb mg.st matches 2.. run return run function mg:core/draw
execute as @a[tag=mg.play] if score @s mg.gft = $gfmin mg.st run function mg:core/win_player
