execute store result storage mg:ev hp int 120 if entity @a[tag=mg.evl]
execute store result score $evhp mg.st run data get storage mg:ev hp
execute if score $evhp mg.st matches ..199 run data modify storage mg:ev hp set value 200
execute if score $evhp mg.st matches 1001.. run data modify storage mg:ev hp set value 1000
execute in minecraft:overworld run function mg:lobby/ev/e1_summon with storage mg:ev
give @a[tag=mg.evl] minecraft:iron_sword[minecraft:item_name={"text":"⚔ Épée du spawn","color":"red"},minecraft:unbreakable={},minecraft:custom_data={mg_ev:1b}]
bossbar set mg:ev color red
title @a[tag=mg.evl] title {"text":"👑 LE ROI ZOMBIE","color":"red","bold":true}
title @a[tag=mg.evl] subtitle {"text":"Prends l'épée et tape-le !","color":"gray"}
execute as @a[tag=mg.evl] at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.7 1.3
