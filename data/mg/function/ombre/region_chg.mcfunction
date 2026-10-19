# @s change de région : titre
scoreboard players operation @s mg.olrg = $r mg.st
title @s times 10 50 15
execute if score $r mg.st matches 0 run title @s title {"text":"HAVRECLAIR","color":"gold","bold":true}
execute if score $r mg.st matches 0 run title @s subtitle {"text":"Cité-refuge","color":"gray"}
execute if score $r mg.st matches 1 run title @s title {"text":"PLAINES DE VALDOR","color":"green","bold":true}
execute if score $r mg.st matches 1 run title @s subtitle {"text":"Niveaux conseillés 1 à 4","color":"gray"}
execute if score $r mg.st matches 2 run title @s title {"text":"FORÊT DE SYLVANOR","color":"dark_green","bold":true}
execute if score $r mg.st matches 2 run title @s subtitle {"text":"Niveaux conseillés 4 à 8","color":"gray"}
execute if score $r mg.st matches 3 run title @s title {"text":"PICS DE GIVRECROC","color":"aqua","bold":true}
execute if score $r mg.st matches 3 run title @s subtitle {"text":"Niveaux conseillés 8 à 12","color":"gray"}
execute if score $r mg.st matches 4 run title @s title {"text":"MARAIS DE FANGEBRUME","color":"dark_aqua","bold":true}
execute if score $r mg.st matches 4 run title @s subtitle {"text":"Niveaux conseillés 12 à 16","color":"gray"}
execute if score $r mg.st matches 5 run title @s title {"text":"SABLES D'AZHAR","color":"yellow","bold":true}
execute if score $r mg.st matches 5 run title @s subtitle {"text":"Niveaux conseillés 16 à 20","color":"gray"}
execute if score $r mg.st matches 6 run title @s title {"text":"PYRECENDRE","color":"red","bold":true}
execute if score $r mg.st matches 6 run title @s subtitle {"text":"Niveaux conseillés 20 à 24","color":"gray"}
execute if score $r mg.st matches 7 run title @s title {"text":"KHAZGARDE","color":"gray","bold":true}
execute if score $r mg.st matches 7 run title @s subtitle {"text":"Niveaux conseillés 24 à 28","color":"gray"}
execute if score $r mg.st matches 8 run title @s title {"text":"TERRES D'OMBRE","color":"dark_purple","bold":true}
execute if score $r mg.st matches 8 run title @s subtitle {"text":"Niveaux conseillés 28 à 32","color":"gray"}
execute at @s run playsound minecraft:event.mob_effect.raid_omen ambient @s ~ ~ ~ 0.4 1.4
