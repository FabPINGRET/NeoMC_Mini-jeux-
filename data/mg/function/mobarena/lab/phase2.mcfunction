# Phase 2 : bouclier d'invulnérabilité tant qu'il reste un alambic
tag @e[tag=mg.boss] add mg.ph2
tag @e[tag=mg.boss] add mg.shield
data modify entity @e[tag=mg.boss,limit=1] Invulnerable set value 1b
summon minecraft:slime 15.0 66 9515.0 {Tags:["mg.alembic"],NoAI:1b,Size:3,PersistenceRequired:1b,Silent:1b,CustomName:[{"text":"Alambic","color":"green","bold":true}],CustomNameVisible:1b}
summon minecraft:slime -14.0 66 9515.0 {Tags:["mg.alembic"],NoAI:1b,Size:3,PersistenceRequired:1b,Silent:1b,CustomName:[{"text":"Alambic","color":"green","bold":true}],CustomNameVisible:1b}
summon minecraft:slime 15.0 66 9486.0 {Tags:["mg.alembic"],NoAI:1b,Size:3,PersistenceRequired:1b,Silent:1b,CustomName:[{"text":"Alambic","color":"green","bold":true}],CustomNameVisible:1b}
summon minecraft:slime -14.0 66 9486.0 {Tags:["mg.alembic"],NoAI:1b,Size:3,PersistenceRequired:1b,Silent:1b,CustomName:[{"text":"Alambic","color":"green","bold":true}],CustomNameVisible:1b}
function mg:mobarena/lab/alembic_hp
bossbar set mg:boss color yellow
title @a[tag=!mg.surv] title [{"text":"PHASE II","color":"dark_green","bold":true}]
title @a[tag=!mg.surv] subtitle [{"text":"Brisez les 4 alambics pour percer son bouclier !","color":"yellow"}]
tellraw @a [{"text":"  ☠ ","color":"dark_red"},{"text":"L'Abomination est protégée ! Détruisez les 4 alambics aux coins de la salle.","color":"green","bold":true}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.beacon.activate master @s ~ ~ ~ 1 0.6
