# Défense de l'outpost Bravo : chaque seconde
scoreboard players remove $tvot2 mg.st 1
scoreboard players remove $tvow2 mg.st 1
execute if score $tvow2 mg.st matches ..0 run function mg:terra/d_wave_2
execute if score $tvot2 mg.st matches 45 unless entity @e[tag=mg.tvcarno] positioned -71.5 68 -9.5 run function mg:terra/d_boss
execute store result score $tvc2 mg.st if entity @e[tag=mg.tvhos,x=-71.5,y=70,z=6.5,distance=..3.5]
scoreboard players operation $tvc2 mg.st *= #4 mg.st
scoreboard players operation $tvoi2 mg.st -= $tvc2 mg.st
execute if score $tvc2 mg.st matches 1.. run particle minecraft:electric_spark -71.5 71.5 6.5 0.3 0.6 0.3 0.4 25
execute if score $tvc2 mg.st matches 1.. run playsound minecraft:entity.iron_golem.damage hostile @a -71.5 70 6.5 0.8 1.4
execute store result bossbar mg:tvo2 value run scoreboard players get $tvoi2 mg.st
bossbar set mg:tvo2 name [{"text":"🛡 Outpost Bravo : générateur ","color":"aqua"},{"score":{"name":"$tvoi2","objective":"mg.st"},"color":"white","bold":true},{"text":" %  ·  ","color":"gray"},{"score":{"name":"$tvot2","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"yellow"}]
bossbar set mg:tvo2 players @a[tag=mg.tvw,x=-71.5,y=70,z=6.5,distance=..56]
execute unless entity @a[tag=mg.tvw,x=-71.5,y=70,z=6.5,distance=..56] run scoreboard players add $tvoa2 mg.st 1
execute if entity @a[tag=mg.tvw,x=-71.5,y=70,z=6.5,distance=..56] run scoreboard players set $tvoa2 mg.st 0
execute if score $tvoa2 mg.st matches 15.. run return run function mg:terra/d_fail_2
execute if score $tvoi2 mg.st matches ..0 run return run function mg:terra/d_fail_2
execute if score $tvot2 mg.st matches ..0 run function mg:terra/d_win_2
