# Une seconde : points pour le roi (seul) ou l'équipe (seule) sur le sommet
execute if score $khm mg.st matches 0 if score $khn mg.st matches 1 run scoreboard players add @a[tag=mg.khz] mg.kh 1
execute if score $khm mg.st matches 1 if score $khr mg.st matches 1.. if score $khb mg.st matches 0 run scoreboard players add Rouge mg.kh 1
execute if score $khm mg.st matches 1 if score $khb mg.st matches 1.. if score $khr mg.st matches 0 run scoreboard players add Bleu mg.kh 1
execute if score $khm mg.st matches 0 if score $khn mg.st matches 1 run title @a[tag=mg.play] actionbar [{"text":"👑 Roi : ","color":"gold"},{"selector":"@a[tag=mg.khz]","color":"yellow"}]
execute if score $khm mg.st matches 1 if score $khr mg.st matches 1.. if score $khb mg.st matches 0 run title @a[tag=mg.play] actionbar {"text":"👑 Les ROUGES tiennent la colline","color":"red"}
execute if score $khm mg.st matches 1 if score $khb mg.st matches 1.. if score $khr mg.st matches 0 run title @a[tag=mg.play] actionbar {"text":"👑 Les BLEUS tiennent la colline","color":"blue"}
execute if score $khn mg.st matches 2.. unless score $khr mg.st matches 1.. run title @a[tag=mg.play] actionbar {"text":"⚔ Sommet contesté !","color":"gray"}
execute if score $khm mg.st matches 1 if score $khr mg.st matches 1.. if score $khb mg.st matches 1.. run title @a[tag=mg.play] actionbar {"text":"⚔ Sommet contesté !","color":"gray"}
execute positioned 0 86 20400 run particle minecraft:happy_villager ~ ~0.5 ~ 2 0.3 2 0 6
execute if score $state mg.st matches 2 if score $khm mg.st matches 0 as @a[tag=mg.play,scores={mg.kh=60..},limit=1] run return run function mg:core/win_player
execute if score $state mg.st matches 2 if score $khm mg.st matches 1 if score Rouge mg.kh matches 90.. run return run function mg:core/win_red
execute if score $state mg.st matches 2 if score $khm mg.st matches 1 if score Bleu mg.kh matches 90.. run return run function mg:core/win_blue
