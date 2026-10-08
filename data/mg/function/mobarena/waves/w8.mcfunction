# Vague 8 — 8 squelettes + 5 wither squelettes
summon minecraft:skeleton 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:skeleton -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:bow",count:1}}}
summon minecraft:wither_skeleton 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:stone_sword",count:1}}}
summon minecraft:wither_skeleton -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:stone_sword",count:1}}}
summon minecraft:wither_skeleton 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:stone_sword",count:1}}}
summon minecraft:wither_skeleton -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:stone_sword",count:1}}}
summon minecraft:wither_skeleton 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:stone_sword",count:1}}}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"8× Squelette archer, 5× Wither squelette","color":"yellow"},{"text":"  (13 monstres)","color":"dark_gray"}]
