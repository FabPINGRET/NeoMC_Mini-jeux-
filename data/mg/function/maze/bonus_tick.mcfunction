# @s : emplacement de bonus (mg.jt = temps avant retour)
execute if score @s mg.jt matches 1.. run return run scoreboard players remove @s mg.jt 1
execute unless entity @e[type=minecraft:item_display,tag=mg.jbd,distance=..1] run function mg:maze/bonus_show
execute as @a[tag=mg.play,gamemode=adventure,distance=..1.2,limit=1,sort=nearest] run function mg:maze/bonus_take
