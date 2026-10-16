# @s change de région ($r) : accès selon la campagne, titre de la région
execute if score $r mg.st matches 1 unless score @s mg.trch matches 30.. unless entity @s[tag=mg.trfree] run return run function mg:terra/rpg/deny_1
execute if score $r mg.st matches 2 unless score @s mg.trch matches 50.. unless entity @s[tag=mg.trfree] run return run function mg:terra/rpg/deny_2
execute if score $r mg.st matches 3 unless score @s mg.trch matches 60.. unless entity @s[tag=mg.trfree] run return run function mg:terra/rpg/deny_3
execute if score $r mg.st matches 4 unless score @s mg.trch matches 70.. unless entity @s[tag=mg.trfree] run return run function mg:terra/rpg/deny_4
scoreboard players operation @s mg.trrg = $r mg.st
title @s times 10 50 15
execute if score $r mg.st matches 0 run title @s title {"text":"VALLÉE DE LA COLONIE","color":"green","bold":true}
execute if score $r mg.st matches 0 run title @s subtitle {"text":"Terres des colons · niveau 1 et plus","color":"gray"}
execute if score $r mg.st matches 1 run title @s title {"text":"MARAIS DES BRUMES","color":"dark_aqua","bold":true}
execute if score $r mg.st matches 1 run title @s subtitle {"text":"Niveau conseillé 4","color":"gray"}
execute if score $r mg.st matches 1 at @s run playsound minecraft:event.mob_effect.raid_omen ambient @s ~ ~ ~ 0.5 1.4
execute if score $r mg.st matches 2 run title @s title {"text":"PLAINES D'AMBRE","color":"gold","bold":true}
execute if score $r mg.st matches 2 run title @s subtitle {"text":"Niveau conseillé 8","color":"gray"}
execute if score $r mg.st matches 2 at @s run playsound minecraft:event.mob_effect.raid_omen ambient @s ~ ~ ~ 0.5 1.4
execute if score $r mg.st matches 3 run title @s title {"text":"CANYON DES RENÉGATS","color":"red","bold":true}
execute if score $r mg.st matches 3 run title @s subtitle {"text":"Niveau conseillé 12","color":"gray"}
execute if score $r mg.st matches 3 at @s run playsound minecraft:event.mob_effect.raid_omen ambient @s ~ ~ ~ 0.5 1.4
execute if score $r mg.st matches 4 run title @s title {"text":"MONT CENDRE","color":"dark_red","bold":true}
execute if score $r mg.st matches 4 run title @s subtitle {"text":"Niveau conseillé 16","color":"gray"}
execute if score $r mg.st matches 4 at @s run playsound minecraft:event.mob_effect.raid_omen ambient @s ~ ~ ~ 0.5 1.4
