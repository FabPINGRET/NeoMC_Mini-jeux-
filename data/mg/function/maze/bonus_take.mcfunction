# @s prend le bonus de l'emplacement le plus proche
tag @e[type=minecraft:marker,tag=mg.jbm,sort=nearest,limit=1] add mg.jbt
execute if entity @e[tag=mg.jbt,tag=mg.jb1] run title @s actionbar {"text":"⚡ Vitesse (10 s)","color":"aqua","bold":true}
execute if entity @e[tag=mg.jbt,tag=mg.jb2] run title @s actionbar {"text":"🧭 Boussole vers la sortie (30 s)","color":"gold","bold":true}
execute if entity @e[tag=mg.jbt,tag=mg.jb3] run title @s actionbar {"text":"🦅 Vue d'aigle (6 s)","color":"green","bold":true}
execute if entity @e[tag=mg.jbt,tag=mg.jb1] run effect give @s minecraft:speed 10 1 true
execute if entity @e[tag=mg.jbt,tag=mg.jb2] run function mg:maze/compass
execute if entity @e[tag=mg.jbt,tag=mg.jb3] run function mg:maze/eagle
execute at @e[tag=mg.jbt] run kill @e[type=minecraft:item_display,tag=mg.jbd,distance=..1]
scoreboard players set @e[tag=mg.jbt] mg.jt 600
tag @e[tag=mg.jbt] remove mg.jbt
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.3
