# Défense de l'outpost Alpha : chaque seconde
scoreboard players remove $tvot1 mg.st 1
scoreboard players remove $tvow1 mg.st 1
execute if score $tvow1 mg.st matches ..0 run function mg:terra/d_wave_1
execute if score $tvot1 mg.st matches 45 unless entity @e[tag=mg.tvcarno] positioned 62.5 70 -87.5 run function mg:terra/d_boss
execute store result score $tvc2 mg.st if entity @e[tag=mg.tvhos,x=62.5,y=65,z=-73.5,distance=..3.5]
scoreboard players operation $tvc2 mg.st *= #4 mg.st
scoreboard players operation $tvoi1 mg.st -= $tvc2 mg.st
execute if score $tvc2 mg.st matches 1.. run particle minecraft:electric_spark 62.5 66.5 -73.5 0.3 0.6 0.3 0.4 25
execute if score $tvc2 mg.st matches 1.. run playsound minecraft:entity.iron_golem.damage hostile @a 62.5 65 -73.5 0.8 1.4
execute store result bossbar mg:tvo1 value run scoreboard players get $tvoi1 mg.st
bossbar set mg:tvo1 name [{"text":"🛡 Outpost Alpha : générateur ","color":"aqua"},{"score":{"name":"$tvoi1","objective":"mg.st"},"color":"white","bold":true},{"text":" %  ·  ","color":"gray"},{"score":{"name":"$tvot1","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"yellow"}]
bossbar set mg:tvo1 players @a[tag=mg.tvw,x=62.5,y=65,z=-73.5,distance=..56]
execute unless entity @a[tag=mg.tvw,x=62.5,y=65,z=-73.5,distance=..56] run scoreboard players add $tvoa1 mg.st 1
execute if entity @a[tag=mg.tvw,x=62.5,y=65,z=-73.5,distance=..56] run scoreboard players set $tvoa1 mg.st 0
execute if score $tvoa1 mg.st matches 15.. run return run function mg:terra/d_fail_1
execute if score $tvoi1 mg.st matches ..0 run return run function mg:terra/d_fail_1
execute if score $tvot1 mg.st matches ..0 run function mg:terra/d_win_1
