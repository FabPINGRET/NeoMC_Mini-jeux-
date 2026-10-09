# Chaque seconde : barre de boss, points de survie, sifflets
scoreboard players operation $cml mg.st = $cmt mg.st
scoreboard players set #20 mg.st 20
execute if score $cmt mg.st matches ..900 run scoreboard players set $cmk mg.st 900
execute if score $cmt mg.st matches 901.. run scoreboard players set $cmk mg.st 4500
scoreboard players operation $cmk mg.st -= $cmt mg.st
execute store result bossbar mg:cham value run scoreboard players get $cmk mg.st
scoreboard players operation $cmk mg.st /= #20 mg.st
scoreboard players set #60 mg.st 60
scoreboard players operation $cmm2 mg.st = $cmk mg.st
scoreboard players operation $cmm2 mg.st /= #60 mg.st
scoreboard players operation $cms2 mg.st = $cmk mg.st
scoreboard players operation $cms2 mg.st %= #60 mg.st
execute store result score $cmh mg.st if entity @a[tag=mg.cmh,tag=!mg.cmout]
execute if score $cmt mg.st matches ..900 if score $cms2 mg.st matches 10.. run bossbar set mg:cham name [{"text":"🦎 Cachez-vous !  ","color":"green","bold":true},{"score":{"name":"$cmm2","objective":"mg.st"},"color":"white"},{"text":":","color":"white"},{"score":{"name":"$cms2","objective":"mg.st"},"color":"white"}]
execute if score $cmt mg.st matches ..900 if score $cms2 mg.st matches ..9 run bossbar set mg:cham name [{"text":"🦎 Cachez-vous !  ","color":"green","bold":true},{"score":{"name":"$cmm2","objective":"mg.st"},"color":"white"},{"text":":0","color":"white"},{"score":{"name":"$cms2","objective":"mg.st"},"color":"white"}]
execute if score $cmt mg.st matches 901.. if score $cms2 mg.st matches 10.. run bossbar set mg:cham name [{"text":"🔍 Chasse  ","color":"red","bold":true},{"score":{"name":"$cmm2","objective":"mg.st"},"color":"white"},{"text":":","color":"white"},{"score":{"name":"$cms2","objective":"mg.st"},"color":"white"},{"text":"   🦎 ","color":"green"},{"score":{"name":"$cmh","objective":"mg.st"},"color":"white"},{"text":" caché(s)","color":"gray"}]
execute if score $cmt mg.st matches 901.. if score $cms2 mg.st matches ..9 run bossbar set mg:cham name [{"text":"🔍 Chasse  ","color":"red","bold":true},{"score":{"name":"$cmm2","objective":"mg.st"},"color":"white"},{"text":":0","color":"white"},{"score":{"name":"$cms2","objective":"mg.st"},"color":"white"},{"text":"   🦎 ","color":"green"},{"score":{"name":"$cmh","objective":"mg.st"},"color":"white"},{"text":" caché(s)","color":"gray"}]
execute as @a[tag=mg.cmh,tag=!mg.cmout] run function mg:cham/hud
scoreboard players operation $cmq mg.st = $cmt mg.st
scoreboard players set #100 mg.st 100
scoreboard players operation $cmq mg.st %= #100 mg.st
execute if score $cmt mg.st matches 901.. if score $cmq mg.st matches 0 run scoreboard players add @a[tag=mg.cmh,tag=!mg.cmout] mg.cmpts 1
scoreboard players operation $cmq mg.st = $cmt mg.st
scoreboard players set #600 mg.st 600
scoreboard players operation $cmq mg.st %= #600 mg.st
execute if score $cmt mg.st matches 901.. if score $cmq mg.st matches 0 run function mg:cham/whistle
execute if score $cmt mg.st matches 700..880 run title @a[tag=mg.cms] actionbar [{"text":"🔍 Libéré dans ","color":"red"},{"score":{"name":"$cms2","objective":"mg.st"},"color":"white","bold":true},{"text":" s","color":"red"}]
execute if score $cmt mg.st matches 700..880 as @a[tag=mg.cms] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 0.6 1.4
