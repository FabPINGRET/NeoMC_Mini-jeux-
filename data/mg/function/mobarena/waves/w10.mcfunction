# Vague 10 — BOSS : ravageur + escorte
summon minecraft:ravager 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,CustomName:[{"text":"LE DÉVOREUR","color":"dark_red","bold":true}],CustomNameVisible:1b}
summon minecraft:vindicator 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:vindicator -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:vindicator 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:vindicator -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:witch 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:witch -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
title @a[tag=!mg.surv] title [{"text":"☠ BOSS ☠","color":"dark_red","bold":true}]
title @a[tag=!mg.surv] subtitle [{"text":"LE DÉVOREUR entre dans l'arène...","color":"red"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.ravager.roar master @s ~ ~ ~ 1 0.8
tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"4× Vindicateur, 2× Sorcière","color":"yellow"},{"text":"  (6 monstres + boss)","color":"dark_gray"}]
tellraw @a [{"text":"  ☠ BOSS : ","color":"dark_red","bold":true},{"text":"LE DÉVOREUR","color":"dark_red","bold":true},{"text":" fait son entrée dans l'arène !","color":"gray"}]
