# @s joue à la machine à sous (déjà payée 50 $) : 55 % rien, 30 % 100 $, 12 % 250 $, 3 % jackpot 1 000 $
execute store result score $gr mg.st run random value 0..99
scoreboard players set $gcv mg.st 0
execute if score $gr mg.st matches 55..84 run scoreboard players set $gcv mg.st 100
execute if score $gr mg.st matches 85..96 run scoreboard players set $gcv mg.st 250
execute if score $gr mg.st matches 97.. run scoreboard players set $gcv mg.st 1000
scoreboard players operation @s mg.gta += $gcv mg.st
scoreboard players set @s mg.gal 40
execute if score $gcv mg.st matches 0 run title @s actionbar {"text":"🎰 🍋 🍒 🔔 … perdu !","color":"gray"}
execute if score $gcv mg.st matches 100 run title @s actionbar {"text":"🎰 🍒 🍒 🍋 … +100 $","color":"green","bold":true}
execute if score $gcv mg.st matches 250 run title @s actionbar {"text":"🎰 🔔 🔔 🔔 … +250 $ !","color":"gold","bold":true}
execute if score $gcv mg.st matches 1000 run title @s title {"text":"💰 JACKPOT 💰","color":"gold","bold":true}
execute if score $gcv mg.st matches 1000 run tellraw @a[tag=mg.gtw] [{"selector":"@s","color":"yellow"},{"text":" a touché le JACKPOT du casino : 1 000 $ !","color":"gold"}]
execute if score $gcv mg.st matches 1.. at @s run playsound minecraft:entity.player.levelup player @s ~ ~ ~ 1 1.4
execute if score $gcv mg.st matches 0 at @s run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 1 0.6
