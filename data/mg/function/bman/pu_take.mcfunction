# @s ramasse le bonus mg.ypt
execute if entity @e[tag=mg.ypt,tag=mg.yp1] if score @s mg.yn matches ..7 run scoreboard players add @s mg.yn 1
execute if entity @e[tag=mg.ypt,tag=mg.yp2] if score @s mg.yr matches ..7 run scoreboard players add @s mg.yr 1
execute if entity @e[tag=mg.ypt,tag=mg.yp3] if score @s mg.yv matches ..3 run function mg:bman/speed_up
execute if entity @e[tag=mg.ypt,tag=mg.yp1] run title @s actionbar {"text":"💣 +1 bombe","color":"red","bold":true}
execute if entity @e[tag=mg.ypt,tag=mg.yp2] run title @s actionbar {"text":"🔥 +1 portée","color":"gold","bold":true}
execute if entity @e[tag=mg.ypt,tag=mg.yp3] run title @s actionbar {"text":"⚡ Vitesse","color":"aqua","bold":true}
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.4
kill @e[tag=mg.ypt]
