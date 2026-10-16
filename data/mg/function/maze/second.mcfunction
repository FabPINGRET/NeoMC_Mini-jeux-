# Chaque seconde : boussole, chrono
scoreboard players remove @a[scores={mg.jk=1..}] mg.jk 1
execute as @a[scores={mg.jk=0}] run clear @s minecraft:compass
scoreboard players set $js mg.st 300
scoreboard players operation $jq mg.st = $jtm mg.st
scoreboard players operation $jq mg.st /= #20 mg.st
scoreboard players operation $js mg.st -= $jq mg.st
execute if score $js mg.st matches 0.. run title @a[tag=mg.play,scores={mg.je=0}] actionbar [{"text":"🌀 ⏱ ","color":"light_purple"},{"score":{"name":"$js","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gray"}]
kill @e[type=minecraft:item,x=-50,y=55,z=41050,dx=100,dy=40,dz=100]
