# @s : les rouleaux sont arrêtés, paiement
scoreboard players operation $gbet mg.st = @s mg.gsb
scoreboard players operation $gr mg.st = @s mg.gsr
scoreboard players set #2 mg.st 2
scoreboard players set #5 mg.st 5
scoreboard players set #20 mg.st 20
execute if score $gr mg.st matches ..72 run title @s subtitle [{"text":"-","color":"red"},{"score":{"name":"$gbet","objective":"mg.st"},"color":"red"},{"text":" $","color":"red"}]
execute if score $gr mg.st matches ..72 run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 1 0.6
execute if score $gr mg.st matches 73..92 run scoreboard players operation $gwin mg.st = $gbet mg.st
execute if score $gr mg.st matches 73..92 run scoreboard players operation $gwin mg.st *= #2 mg.st
execute if score $gr mg.st matches 73..92 run scoreboard players operation @s mg.gta += $gwin mg.st
execute if score $gr mg.st matches 93..98 run scoreboard players operation $gwin mg.st = $gbet mg.st
execute if score $gr mg.st matches 93..98 run scoreboard players operation $gwin mg.st *= #5 mg.st
execute if score $gr mg.st matches 93..98 run scoreboard players operation @s mg.gta += $gwin mg.st
execute if score $gr mg.st matches 99 run scoreboard players operation $gwin mg.st = $gbet mg.st
execute if score $gr mg.st matches 99 run scoreboard players operation $gwin mg.st *= #20 mg.st
execute if score $gr mg.st matches 99 run scoreboard players operation @s mg.gta += $gwin mg.st
execute if score $gr mg.st matches 73.. run title @s subtitle [{"text":"+","color":"green"},{"score":{"name":"$gwin","objective":"mg.st"},"color":"green","bold":true},{"text":" $","color":"green"}]
execute if score $gr mg.st matches 73.. run playsound minecraft:entity.player.levelup player @a ~ ~ ~ 1 1.3
execute if score $gr mg.st matches 73.. run particle minecraft:happy_villager ~ ~1.5 ~ 0.6 0.6 0.6 0 25
execute if score $gr mg.st matches 93.. run particle minecraft:wax_off ~ ~2 ~ 0.8 0.8 0.8 0.5 40
execute if score $gr mg.st matches 99 run particle minecraft:totem_of_undying ~ ~1.5 ~ 0.5 1 0.5 0.6 120
execute if score $gr mg.st matches 99 run playsound minecraft:ui.toast.challenge_complete player @a ~ ~ ~ 1 1
execute if score $gr mg.st matches 99 run tellraw @a[tag=mg.gtw] [{"selector":"@s","color":"yellow"},{"text":" touche le JACKPOT au casino : ","color":"gold"},{"score":{"name":"$gwin","objective":"mg.st"},"color":"green","bold":true},{"text":" $ !","color":"gold"}]
