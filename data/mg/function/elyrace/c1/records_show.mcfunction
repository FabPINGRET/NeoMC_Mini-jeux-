# @s = joueur : son meilleur temps et le record du serveur sur le parcours 1 (Canyon du Couchant)
execute unless score @s mg.xr1 matches 1.. run tellraw @s [{"text":"  ⏱ Canyon du Couchant : ","color":"aqua"},{"text":"pas encore de temps","color":"gray"}]
execute if score @s mg.xr1 matches 1.. run scoreboard players operation #xq mg.st = @s mg.xr1
execute if score @s mg.xr1 matches 1.. run function mg:elyrace/time
execute if score @s mg.xr1 matches 1.. if score $ecs mg.st matches ..9 run tellraw @s [{"text":"  ⏱ Canyon du Couchant : ","color":"aqua"},{"text":"ton record ","color":"gray"},{"score":{"name":"$es","objective":"mg.st"},"color":"gold"},{"text":",","color":"gold"},{"text":"0","color":"gold"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gold"}]
execute if score @s mg.xr1 matches 1.. if score $ecs mg.st matches 10.. run tellraw @s [{"text":"  ⏱ Canyon du Couchant : ","color":"aqua"},{"text":"ton record ","color":"gray"},{"score":{"name":"$es","objective":"mg.st"},"color":"gold"},{"text":",","color":"gold"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gold"}]
# record du serveur : le détenteur et le temps viennent du stockage mg:hall (composant interprété) ; repli : le temps seul
execute if data storage mg:hall e.xr1 run tellraw @s [{"text":"    🏆 ","color":"gold"},{"nbt":"e.xr1","storage":"mg:hall","interpret":true}]
execute if score #srv mg.xr1 matches 1.. unless data storage mg:hall e.xr1 run scoreboard players operation #xq mg.st = #srv mg.xr1
execute if score #srv mg.xr1 matches 1.. unless data storage mg:hall e.xr1 run function mg:elyrace/time
execute if score #srv mg.xr1 matches 1.. unless data storage mg:hall e.xr1 if score $ecs mg.st matches ..9 run tellraw @s [{"text":"    🏆 Record du serveur : ","color":"gold"},{"score":{"name":"$es","objective":"mg.st"},"color":"gold"},{"text":",","color":"gold"},{"text":"0","color":"gold"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gold"}]
execute if score #srv mg.xr1 matches 1.. unless data storage mg:hall e.xr1 if score $ecs mg.st matches 10.. run tellraw @s [{"text":"    🏆 Record du serveur : ","color":"gold"},{"score":{"name":"$es","objective":"mg.st"},"color":"gold"},{"text":",","color":"gold"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gold"}]
