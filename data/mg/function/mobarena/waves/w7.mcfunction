# Vague 7 — 12 zombies + 4 vindicateurs
summon minecraft:zombie 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:vindicator 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:vindicator -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:vindicator 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:vindicator -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"12× Zombie, 4× Vindicateur","color":"yellow"},{"text":"  (16 monstres)","color":"dark_gray"}]
