#Noparentunnels
execute unless entity @s[tag=no_warp] at @s unless entity @s[x=-1000,dx=-20000] if entity @s[x=-1000,dx=2000] run playsound minecraft:block.gravel.break master @s ~ ~ ~ 1 1
execute unless entity @s[tag=no_warp] at @s unless entity @s[x=-1000,dx=-20000] if entity @s[x=-1000,dx=2000] run particle dust_pillar{block_state:"minecraft:coarse_dirt"} ~ ~ ~ 0.4 0 0.4 0.5 200 normal
execute unless entity @s[tag=no_warp] at @s unless entity @s[x=-1000,dx=-20000] if entity @s[x=-1000,dx=2000] run tp @s -208 63 -1187 180 0
execute unless entity @s[tag=no_warp] at @s unless entity @s[x=-1000,dx=-20000] if entity @s[x=-1000,dx=2000] run playsound minecraft:block.gravel.break master @s -208 63 -1187 1 1
execute unless entity @s[tag=no_warp] at @s unless entity @s[x=-1000,dx=-20000] if entity @s[x=-1000,dx=2000] run particle dust_pillar{block_state:"minecraft:coarse_dirt"} -208 63 -1187 0.4 0 0.4 0.5 200 normal

#Dark BuhTween
execute unless entity @s[tag=no_warp] at @s unless entity @s[x=-1000,dx=-20000] if entity @s[x=9000,dx=2000] run playsound minecraft:block.gravel.break master @s ~ ~ ~ 1 1
execute unless entity @s[tag=no_warp] at @s unless entity @s[x=-1000,dx=-20000] if entity @s[x=9000,dx=2000] run particle dust_pillar{block_state:"minecraft:netherrack"} ~ ~ ~ 0.4 0 0.4 0.5 200 normal
execute unless entity @s[tag=no_warp] at @s unless entity @s[x=-1000,dx=-20000] if entity @s[x=9000,dx=2000] run tp @s 9096 179 -1033 180 30
execute unless entity @s[tag=no_warp] at @s unless entity @s[x=-1000,dx=-20000] if entity @s[x=9000,dx=2000] run playsound minecraft:block.gravel.break master @s -208 63 -1187 1 1

execute unless entity @s[tag=no_warp] at @s unless entity @s[x=-1000,dx=-20000] if entity @s[x=9000,dx=2000] run particle dust_pillar{block_state:"minecraft:polished_deepslate"} 9096 179 -1033 0.4 0 0.4 0.5 200 normal
execute unless entity @s[tag=no_warp] at @s unless entity @s[x=-1000,dx=-20000] if entity @s[x=9000,dx=2000] run stopsound @s record minecraft:soundtrack.slime_man_theme

execute if entity @s[tag=no_warp] at @s run tellraw @s {"text":"You can't use this right now...","color":"gray","italic":true}
execute at @s if entity @s[x=-1000,dx=-20000] run tellraw @s {"text":"You can't use this here...","color":"gray","italic":true}
