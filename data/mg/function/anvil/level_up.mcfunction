# Intensité +1 : plus d'enclumes, de plus en plus vite
scoreboard players add $lv mg.st 1
scoreboard players set $lt mg.st 160
scoreboard players set $ai mg.st 28
scoreboard players operation $tmp mg.st = $lv mg.st
scoreboard players operation $tmp mg.st *= $c2 mg.st
scoreboard players operation $ai mg.st -= $tmp mg.st
scoreboard players operation $ai mg.st > $amin mg.st
title @a[tag=mg.play] actionbar [{"text":"⚠ La pluie s'intensifie ! Niveau ","color":"red","bold":true},{"score":{"name":"$lv","objective":"mg.st"},"color":"gold","bold":true}]
execute as @a at @s run playsound minecraft:block.anvil.land master @s ~ ~ ~ 0.4 0.6
