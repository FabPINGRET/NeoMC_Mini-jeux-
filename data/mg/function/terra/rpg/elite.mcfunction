# @s devient une élite : affixe au hasard, PV ×2, contour doré, butin d'élite à sa mort
tag @s add mg.trelite
attribute @s minecraft:max_health modifier add mg:trelite 1 add_multiplied_total
execute store result entity @s Health float 1 run attribute @s minecraft:max_health get
data merge entity @s {DeathLootTable:"mg:terra/elite",CustomNameVisible:1b}
execute store result score $r mg.st run random value 1..3
execute if score $r mg.st matches 1 run effect give @s minecraft:speed infinite 1 true
execute if score $r mg.st matches 1 run effect give @s minecraft:strength infinite 0 true
execute if score $r mg.st matches 1 run data merge entity @s {CustomName:{"text":"★ Élite enragée","color":"gold","bold":true}}
execute if score $r mg.st matches 2 run attribute @s minecraft:scale modifier add mg:trelite 0.35 add_multiplied_base
execute if score $r mg.st matches 2 run attribute @s minecraft:knockback_resistance base set 1
execute if score $r mg.st matches 2 run data merge entity @s {CustomName:{"text":"★ Colosse","color":"gold","bold":true}}
execute if score $r mg.st matches 3 run effect give @s minecraft:regeneration infinite 1 true
execute if score $r mg.st matches 3 run data merge entity @s {CustomName:{"text":"★ Élite régénérante","color":"gold","bold":true}}
scoreboard players operation $tvi mg.st = @s mg.tvid
execute as @e[tag=mg.tvp] if score @s mg.tvid = $tvi mg.st run data merge entity @s {Glowing:1b,glow_color_override:16766720}
