# @s = joueur qui termine un tour
scoreboard players set @s mg.cp 0
scoreboard players add @s mg.lp 1
execute if score @s mg.lp matches 1..2 run tellraw @a[tag=mg.play] [{"selector":"@s","color":"yellow"},{"text":" termine le tour ","color":"gray"},{"score":{"name":"@s","objective":"mg.lp"},"color":"gold"},{"text":" / 3","color":"gray"}]
execute if score @s mg.lp matches 2 run title @s title [{"text":"Dernier tour !","color":"red","bold":true}]
execute if score @s mg.lp matches 1 run title @s actionbar [{"text":"Tour 1 / 3 terminé","color":"green"}]
execute if score @s mg.lp matches 3.. run function mg:icerace/finish
