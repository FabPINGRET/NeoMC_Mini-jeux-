# @s : a cliqué sur le socle de la canne (advancement mg:lobby_fish_take) : prend la canne, ou la range s'il l'a déjà
advancement revoke @s only mg:lobby_fish_take
execute if score $lfoff mg.st matches 1 run return run title @s actionbar {"text":"🎣 Pêche désactivée par un admin.","color":"red"}
execute unless function mg:lobby/fish/keep run return run title @s actionbar {"text":"🎣 Pas possible ici (au spawn, hors activité).","color":"red"}
# canne déjà dans l'inventaire : on la range
execute store result score #lfi mg.st run clear @s *[minecraft:custom_data~{mg_rod:1b}] 0
execute if score #lfi mg.st matches 1.. run clear @s *[minecraft:custom_data~{mg_rod:1b}]
execute if score #lfi mg.st matches 1.. run title @s actionbar {"text":"🎣 Canne rangée.","color":"gray"}
execute if score #lfi mg.st matches 1.. run return 0
scoreboard players add $rod mg.lfn 1
execute if items entity @s hotbar.7 * run give @s minecraft:fishing_rod[custom_data={mg_rod:1b},unbreakable={},custom_name=[{"text":"🎣 Canne du spawn","color":"aqua","bold":true,"italic":false}],lore=[[{"text":"Lance ta ligne dans l'étang : les prises sont virtuelles","color":"gray","italic":false}]]]
execute unless items entity @s hotbar.7 * run item replace entity @s hotbar.7 with minecraft:fishing_rod[custom_data={mg_rod:1b},unbreakable={},custom_name=[{"text":"🎣 Canne du spawn","color":"aqua","bold":true,"italic":false}],lore=[[{"text":"Lance ta ligne dans l'étang : les prises sont virtuelles","color":"gray","italic":false}]]]
title @s actionbar {"text":"🎣 Canne en main : lance-la dans l'étang.","color":"aqua"}
