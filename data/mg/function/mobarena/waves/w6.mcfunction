# Vague 6 — 8 squelettes + 4 bébés zombies (rapides !)
summon minecraft:skeleton 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:zombie 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsBaby:1b}
summon minecraft:zombie -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsBaby:1b}
summon minecraft:zombie 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsBaby:1b}
summon minecraft:zombie -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,IsBaby:1b}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"8× Squelette archer, 4× Zombie","color":"yellow"},{"text":"  (12 monstres)","color":"dark_gray"}]
