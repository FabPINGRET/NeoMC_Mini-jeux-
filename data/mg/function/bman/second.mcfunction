# Chaque seconde : barre d'action, bombe rendue si jetée, objets au sol supprimés
kill @e[type=minecraft:item,x=-12,y=60,z=40689,dx=24,dy=15,dz=22]
execute as @a[tag=mg.play] unless items entity @s container.* *[custom_data~{ybomb:1b}] run function mg:bman/give
scoreboard players set $ys mg.st 240
scoreboard players operation $yq mg.st = $yc mg.st
scoreboard players operation $yq mg.st /= #20 mg.st
scoreboard players operation $ys mg.st -= $yq mg.st
execute as @a[tag=mg.play] run title @s actionbar [{"text":"💣 ","color":"red"},{"score":{"name":"@s","objective":"mg.yn"},"color":"white","bold":true},{"text":"   🔥 ","color":"gold"},{"score":{"name":"@s","objective":"mg.yr"},"color":"white","bold":true},{"text":"   ⚡ ","color":"aqua"},{"score":{"name":"@s","objective":"mg.yv"},"color":"white","bold":true},{"text":"     ⏱ ","color":"gray"},{"score":{"name":"$ys","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gray"}]
