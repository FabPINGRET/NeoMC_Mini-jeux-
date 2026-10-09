# @s : visée — jauge oscillante, aperçu de la trajectoire, clic droit = lancer
scoreboard players operation @s mg.bpw += @s mg.bpd
scoreboard players operation @s mg.bpw += @s mg.bpd
scoreboard players operation @s mg.bpw += @s mg.bpd
scoreboard players operation @s mg.bpw += @s mg.bpd
execute if score @s mg.bpw matches 100.. run scoreboard players set @s mg.bpd -1
execute if score @s mg.bpw matches ..0 run scoreboard players set @s mg.bpd 1
execute unless items entity @s weapon.mainhand *[minecraft:custom_data~{mg_bowl:1b}] unless items entity @s weapon.offhand *[minecraft:custom_data~{mg_bowl:1b}] unless items entity @s hotbar.* *[minecraft:custom_data~{mg_bowl:1b}] unless items entity @s inventory.* *[minecraft:custom_data~{mg_bowl:1b}] run function mg:bowl/give
execute store result score #yw mg.st run data get entity @s Rotation[0] 100
execute if score #yw mg.st matches 18001.. run scoreboard players remove #yw mg.st 36000
execute if score #yw mg.st matches ..-18001 run scoreboard players add #yw mg.st 36000
execute unless items entity @s weapon.mainhand *[minecraft:custom_data~{mg_bowl:1b}] run title @s actionbar {"text":"🎳 Prends la boule en main (barre d'outils)","color":"yellow"}
execute if items entity @s weapon.mainhand *[minecraft:custom_data~{mg_bowl:1b}] unless score #yw mg.st matches -800..800 run title @s actionbar {"text":"🎳 Vise la piste ! (le lancer sera redressé)","color":"red"}
execute if items entity @s weapon.mainhand *[minecraft:custom_data~{mg_bowl:1b}] if score #yw mg.st matches -800..800 run function mg:bowl/gauge
scoreboard players operation #q mg.st = @s mg.btm
scoreboard players set #k mg.st 3
scoreboard players operation #q mg.st %= #k mg.st
execute if score #q mg.st matches 0 if score #yw mg.st matches -800..800 run function mg:bowl/preview
execute if score @s mg.blu matches 1.. if items entity @s weapon.mainhand *[minecraft:custom_data~{mg_bowl:1b}] run return run function mg:bowl/throw
execute if score @s mg.btm matches 500 run title @s actionbar {"text":"🎳 Lance vite : lancer automatique dans 5 s !","color":"red"}
execute if score @s mg.btm matches 600.. run function mg:bowl/throw
