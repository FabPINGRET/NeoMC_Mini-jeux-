# Frag (@s = victime, PV épuisés ; le tireur porte mg.tmsh ; $tmd = dégâts du dernier tir) : +1 au tireur et à son équipe, kill-feed, réapparition immédiate
scoreboard players add @a[tag=mg.tmsh,limit=1] mg.tmk 1
execute if entity @a[tag=mg.tmsh,team=mg_red] run scoreboard players add Rouge mg.tmk 1
execute if entity @a[tag=mg.tmsh,team=mg_blue] run scoreboard players add Bleu mg.tmk 1
execute if entity @a[tag=mg.tmsh,team=mg_red] if score $tmd mg.st matches 2.. run tellraw @a[tag=mg.play] [{"selector":"@a[tag=mg.tmsh,limit=1]","color":"red"},{"text":" 🎯 ","color":"gold"},{"selector":"@s","color":"blue"},{"text":" (tête)","color":"gray"}]
execute if entity @a[tag=mg.tmsh,team=mg_red] if score $tmd mg.st matches ..1 run tellraw @a[tag=mg.play] [{"selector":"@a[tag=mg.tmsh,limit=1]","color":"red"},{"text":" 🎯 ","color":"gold"},{"selector":"@s","color":"blue"},{"text":"","color":"gray"}]
execute if entity @a[tag=mg.tmsh,team=mg_blue] if score $tmd mg.st matches 2.. run tellraw @a[tag=mg.play] [{"selector":"@a[tag=mg.tmsh,limit=1]","color":"blue"},{"text":" 🎯 ","color":"gold"},{"selector":"@s","color":"red"},{"text":" (tête)","color":"gray"}]
execute if entity @a[tag=mg.tmsh,team=mg_blue] if score $tmd mg.st matches ..1 run tellraw @a[tag=mg.play] [{"selector":"@a[tag=mg.tmsh,limit=1]","color":"blue"},{"text":" 🎯 ","color":"gold"},{"selector":"@s","color":"red"},{"text":"","color":"gray"}]
execute as @a[tag=mg.tmsh,limit=1] run title @s actionbar [{"text":"🎯 Frag ! ","color":"green","bold":true},{"score":{"name":"@s","objective":"mg.tmk"},"color":"gold"}]
execute as @a[tag=mg.tmsh,limit=1] at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.2
execute at @s run particle minecraft:firework ~ ~1 ~ 0.3 0.5 0.3 0.15 40
function mg:tdm/spawn
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score Rouge mg.tmk matches 25.. run function mg:core/win_red
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score Bleu mg.tmk matches 25.. run function mg:core/win_blue
