# Phase 2 : 8 tentacules ; le boss est invulnérable tant qu'il en reste un
tag @e[tag=mg.boss] add mg.ph2
tag @e[tag=mg.boss] add mg.shield
data modify entity @e[tag=mg.boss,limit=1] Invulnerable set value 1b
summon minecraft:slime 12.9 63 9905.5 {Tags:["mg.mob","mg.tent"],PersistenceRequired:1b,Size:3,CustomName:[{"text":"Tentacule","color":"dark_aqua","bold":true}],CustomNameVisible:1b}
summon minecraft:slime 5.3 63 9913.0 {Tags:["mg.mob","mg.tent"],PersistenceRequired:1b,Size:3,CustomName:[{"text":"Tentacule","color":"dark_aqua","bold":true}],CustomNameVisible:1b}
summon minecraft:slime -5.5 63 9912.9 {Tags:["mg.mob","mg.tent"],PersistenceRequired:1b,Size:3,CustomName:[{"text":"Tentacule","color":"dark_aqua","bold":true}],CustomNameVisible:1b}
summon minecraft:slime -13.0 63 9905.3 {Tags:["mg.mob","mg.tent"],PersistenceRequired:1b,Size:3,CustomName:[{"text":"Tentacule","color":"dark_aqua","bold":true}],CustomNameVisible:1b}
summon minecraft:slime -12.9 63 9894.5 {Tags:["mg.mob","mg.tent"],PersistenceRequired:1b,Size:3,CustomName:[{"text":"Tentacule","color":"dark_aqua","bold":true}],CustomNameVisible:1b}
summon minecraft:slime -5.3 63 9887.0 {Tags:["mg.mob","mg.tent"],PersistenceRequired:1b,Size:3,CustomName:[{"text":"Tentacule","color":"dark_aqua","bold":true}],CustomNameVisible:1b}
summon minecraft:slime 5.5 63 9887.1 {Tags:["mg.mob","mg.tent"],PersistenceRequired:1b,Size:3,CustomName:[{"text":"Tentacule","color":"dark_aqua","bold":true}],CustomNameVisible:1b}
summon minecraft:slime 13.0 63 9894.7 {Tags:["mg.mob","mg.tent"],PersistenceRequired:1b,Size:3,CustomName:[{"text":"Tentacule","color":"dark_aqua","bold":true}],CustomNameVisible:1b}
function mg:mobarena/temple/tent_hp
bossbar set mg:boss color yellow
title @a[tag=!mg.surv] title [{"text":"PHASE II","color":"dark_aqua","bold":true}]
title @a[tag=!mg.surv] subtitle [{"text":"Détruisez les 8 tentacules !","color":"yellow"}]
tellraw @a [{"text":"  ☠ ","color":"dark_red"},{"text":"L'Émissaire invoque ses tentacules : il est invulnérable tant que l'un d'eux vit !","color":"aqua","bold":true}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.elder_guardian.curse master @s ~ ~ ~ 1 0.7
