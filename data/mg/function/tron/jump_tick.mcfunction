# @s (moto) : recharge du saut, clic droit = saut armé 3 s (Espace pour sauter)
scoreboard players remove @s[scores={mg.trj=1..}] mg.trj 1
scoreboard players operation $tid mg.st = @s mg.trc
execute if score @s mg.trj matches 1.. if score @s mg.qs matches 1.. run title @s actionbar [{"text":"⤴ Saut en recharge : ","color":"gray"},{"score":{"name":"@s","objective":"mg.trj"},"color":"yellow"},{"text":" ticks","color":"gray"}]
execute if score @s mg.trj matches ..0 if score @s mg.qs matches 1.. run function mg:tron/jump_arm
execute if score @s mg.trj matches 340 as @e[tag=mg.trh] if score @s mg.trc = $tid mg.st run attribute @s minecraft:jump_strength base set 0
execute if score @s mg.trj matches 1 run title @s actionbar {"text":"⤴ Saut prêt (clic droit)","color":"green"}
