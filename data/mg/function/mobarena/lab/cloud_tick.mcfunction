# Nuage de peste (@s = marqueur)
scoreboard players remove @s mg.cd 1
execute if score @s mg.cd matches ..0 run return run kill @s
execute if entity @s[tag=!mg.big] run particle minecraft:sneeze ~ ~0.3 ~ 1.2 0.3 1.2 0 4
execute if entity @s[tag=!mg.big] run effect give @a[tag=mg.play,distance=..2.8] minecraft:poison 2 1 true
execute if entity @s[tag=mg.big] run particle minecraft:sneeze ~ ~0.4 ~ 2.4 0.4 2.4 0 12
execute if entity @s[tag=mg.big] run particle minecraft:happy_villager ~ ~0.8 ~ 2.4 0.6 2.4 0 2
execute if entity @s[tag=mg.big] run effect give @a[tag=mg.play,distance=..4.2] minecraft:poison 2 2 true
execute if entity @s[tag=mg.big] run effect give @a[tag=mg.play,distance=..4.2] minecraft:nausea 6 0 true
