# Vague 9 — 10 zombies + 5 vindicateurs + 3 sorcières
summon minecraft:zombie 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:zombie 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:vindicator 11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:vindicator -11.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:vindicator 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:vindicator -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:vindicator 0.5 64 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_axe",count:1}}}
summon minecraft:witch 11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:witch -11.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:witch 0.5 64 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"10× Zombie, 5× Vindicateur, 3× Sorcière","color":"yellow"},{"text":"  (18 monstres)","color":"dark_gray"}]
