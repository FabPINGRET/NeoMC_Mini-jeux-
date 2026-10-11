bossbar set mg:ev name {"text":"🗝 Chasse au trésor","color":"aqua","bold":true}
execute store result bossbar mg:ev value run scoreboard players get $evt mg.st
execute as @a[tag=mg.evl] run title @s actionbar {"text":"❄ Froid","color":"blue"}
execute at @e[type=minecraft:marker,tag=mg.evt] as @a[tag=mg.evl,distance=..45] run title @s actionbar {"text":"🌡 Tiède","color":"yellow"}
execute at @e[type=minecraft:marker,tag=mg.evt] as @a[tag=mg.evl,distance=..22] run title @s actionbar {"text":"🔥 Chaud !","color":"gold"}
execute at @e[type=minecraft:marker,tag=mg.evt] as @a[tag=mg.evl,distance=..9] run title @s actionbar {"text":"🔥🔥 Brûlant !!","color":"red","bold":true}
execute if score $evt mg.st matches 90 run data merge entity @e[type=minecraft:item_display,tag=mg.evtc,limit=1] {Glowing:1b,glow_color_override:16766720}
execute if score $evt mg.st matches 90 run tellraw @a[tag=mg.evl] {"text":"🗝 Indice : le coffre brille maintenant !","color":"aqua"}
execute if score $evt mg.st matches 45 at @e[type=minecraft:marker,tag=mg.evt] run summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:25,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:2,explosions:[{shape:"burst",colors:[I;65535]}]}}}}
execute if score $evt mg.st matches 45 run tellraw @a[tag=mg.evl] {"text":"🗝 Indice : regarde la fusée !","color":"aqua"}
execute at @e[type=minecraft:marker,tag=mg.evt] run particle minecraft:end_rod ~ ~0.5 ~ 0.3 0.3 0.3 0.01 2
