# Départ : 45 s pour se cacher
scoreboard players set $cmt mg.st 0
scoreboard players set $cmc mg.st 0
scoreboard players set $cmdc mg.st 0
execute as @a[tag=mg.cmh] run function mg:cham/become
execute as @a[tag=mg.cms] run function mg:cham/seeker_kit
effect give @a[tag=mg.cms] minecraft:blindness 46 0 true
bossbar add mg:cham {"text":"🦎 Meccha Chameleon"}
bossbar set mg:cham color green
bossbar set mg:cham max 900
bossbar set mg:cham players @a[tag=mg.cmx]
execute as @a[tag=mg.cmh] run function mg:cham/help_hider
execute as @a[tag=mg.cms] run function mg:cham/help_seeker
title @a[tag=mg.cmh] title {"text":"🦎 Cache-toi !","color":"green","bold":true}
title @a[tag=mg.cmh] subtitle {"text":"Peins-toi aux couleurs du décor","color":"gray"}
title @a[tag=mg.cms] title {"text":"🔍 Chasseur","color":"red","bold":true}
title @a[tag=mg.cms] subtitle {"text":"Libéré dans 45 s","color":"gray"}
execute if score $cmsolo mg.st matches 1 run tellraw @a[tag=mg.cmx] {"text":"🦎 Mode entraînement (seul) : tu es caméléon, essaie la palette, la pipette et les poses. Il faut au moins 2 joueurs pour une vraie partie.","color":"yellow"}
