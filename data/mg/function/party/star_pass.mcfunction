# Passage sur l'étoile (@s) : achat automatique à 20 pièces, l'étoile change ensuite de place
execute if score @s mg.mpm matches ..19 run return run tellraw @s [{"text":"★ L'étoile coûte 20 pièces : reviens plus riche !","color":"yellow"}]
scoreboard players remove @s mg.mpm 20
scoreboard players add @s mg.mpk 1
title @a[tag=mg.mpp] title [{"text":"★","color":"yellow","bold":true}]
title @a[tag=mg.mpp] subtitle [{"selector":"@s","color":"yellow"},{"text":" obtient une étoile !","color":"gold"}]
tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"yellow"},{"selector":"@s","color":"yellow","bold":true},{"text":" achète une étoile pour 20 pièces !","color":"gold"}]
execute as @a[tag=mg.mpp] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1.2
execute at @e[type=minecraft:armor_stand,tag=mg.mpfocus,limit=1] run particle minecraft:firework ~ ~1 ~ 0.5 1 0.5 0.1 60
function mg:party/star_move
