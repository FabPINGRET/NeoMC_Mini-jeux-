# Défense de l'outpost Charlie : chaque seconde
scoreboard players remove $tvot3 mg.st 1
scoreboard players remove $tvow3 mg.st 1
execute if score $tvow3 mg.st matches ..0 run function mg:terra/d_wave_3
execute if score $tvot3 mg.st matches 45 unless entity @e[tag=mg.tvcarno] positioned 30.5 63 56.5 run function mg:terra/d_boss
execute store result score $tvc2 mg.st if entity @e[tag=mg.tvhos,x=30.5,y=66,z=72.5,distance=..3.5]
scoreboard players operation $tvc2 mg.st *= #4 mg.st
scoreboard players operation $tvoi3 mg.st -= $tvc2 mg.st
execute if score $tvc2 mg.st matches 1.. run particle minecraft:electric_spark 30.5 67.5 72.5 0.3 0.6 0.3 0.4 25
execute if score $tvc2 mg.st matches 1.. run playsound minecraft:entity.iron_golem.damage hostile @a 30.5 66 72.5 0.8 1.4
execute store result bossbar mg:tvo3 value run scoreboard players get $tvoi3 mg.st
bossbar set mg:tvo3 name [{"text":"🛡 Outpost Charlie : générateur ","color":"aqua"},{"score":{"name":"$tvoi3","objective":"mg.st"},"color":"white","bold":true},{"text":" %  ·  ","color":"gray"},{"score":{"name":"$tvot3","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"yellow"}]
bossbar set mg:tvo3 players @a[tag=mg.tvw,x=30.5,y=66,z=72.5,distance=..56]
execute unless entity @a[tag=mg.tvw,x=30.5,y=66,z=72.5,distance=..56] run scoreboard players add $tvoa3 mg.st 1
execute if entity @a[tag=mg.tvw,x=30.5,y=66,z=72.5,distance=..56] run scoreboard players set $tvoa3 mg.st 0
execute if score $tvoa3 mg.st matches 15.. run return run function mg:terra/d_fail_3
execute if score $tvoi3 mg.st matches ..0 run return run function mg:terra/d_fail_3
execute if score $tvot3 mg.st matches ..0 run function mg:terra/d_win_3
