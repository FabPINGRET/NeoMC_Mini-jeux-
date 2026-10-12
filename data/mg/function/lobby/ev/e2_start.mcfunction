scoreboard players set $evt mg.st 60
bossbar set mg:ev max 60
execute unless score $theme mg.st matches 1..2 run bossbar set mg:ev color yellow
execute if score $theme mg.st matches 1 run bossbar set mg:ev color yellow
execute if score $theme mg.st matches 2 run bossbar set mg:ev color red
execute unless score $theme mg.st matches 1..2 run title @a[tag=mg.evl] title {"text":"💰 PLUIE DE PIÈCES","color":"gold","bold":true}
execute if score $theme mg.st matches 1 run title @a[tag=mg.evl] title {"text":"🍬 CHASSE AUX BONBONS","color":"gold","bold":true}
execute if score $theme mg.st matches 2 run title @a[tag=mg.evl] title {"text":"🎁 CHASSE AUX CADEAUX","color":"red","bold":true}
title @a[tag=mg.evl] subtitle {"text":"Ramasse tout ce qui tombe !","color":"gray"}
