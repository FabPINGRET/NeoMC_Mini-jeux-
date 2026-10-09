# Machine à sous : 73 % perdu, 20 % ×2, 6 % ×5, 1 % ×20 (la maison garde ~10 %)
execute store result score $gr mg.st run random value 0..99
execute if score $gr mg.st matches ..72 run title @s title {"text":"🍋  🍒  🔔","bold":true}
execute if score $gr mg.st matches ..72 run title @s subtitle [{"text":"-","color":"red"},{"score":{"name":"$gbet","objective":"mg.st"},"color":"red"},{"text":" $","color":"red"}]
execute if score $gr mg.st matches ..72 at @s run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 1 0.6
scoreboard players set #2 mg.st 2
scoreboard players set #5 mg.st 5
scoreboard players set #20 mg.st 20
execute if score $gr mg.st matches 73..92 run title @s title {"text":"🍒  🍒  🍋","bold":true}
execute if score $gr mg.st matches 73..92 run scoreboard players operation $gwin mg.st = $gbet mg.st
execute if score $gr mg.st matches 73..92 run scoreboard players operation $gwin mg.st *= #2 mg.st
execute if score $gr mg.st matches 73..92 run scoreboard players operation @s mg.gta += $gwin mg.st
execute if score $gr mg.st matches 93..98 run title @s title {"text":"🔔  🔔  🔔","color":"gold","bold":true}
execute if score $gr mg.st matches 93..98 run scoreboard players operation $gwin mg.st = $gbet mg.st
execute if score $gr mg.st matches 93..98 run scoreboard players operation $gwin mg.st *= #5 mg.st
execute if score $gr mg.st matches 93..98 run scoreboard players operation @s mg.gta += $gwin mg.st
execute if score $gr mg.st matches 99 run title @s title {"text":"7️⃣  7️⃣  7️⃣","color":"red","bold":true}
execute if score $gr mg.st matches 99 run scoreboard players operation $gwin mg.st = $gbet mg.st
execute if score $gr mg.st matches 99 run scoreboard players operation $gwin mg.st *= #20 mg.st
execute if score $gr mg.st matches 99 run scoreboard players operation @s mg.gta += $gwin mg.st
execute if score $gr mg.st matches 99 run tellraw @a[tag=mg.gtw] [{"selector":"@s","color":"yellow"},{"text":" touche le JACKPOT au casino : ","color":"gold"},{"score":{"name":"$gwin","objective":"mg.st"},"color":"green","bold":true},{"text":" $ !","color":"gold"}]
execute if score $gr mg.st matches 73.. run title @s subtitle [{"text":"+","color":"green"},{"score":{"name":"$gwin","objective":"mg.st"},"color":"green","bold":true},{"text":" $","color":"green"}]
execute if score $gr mg.st matches 73.. at @s run playsound minecraft:entity.player.levelup player @s ~ ~ ~ 1 1.3
function mg:gta/cas_reopen {d:"slot"}
