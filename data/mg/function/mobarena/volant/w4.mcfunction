# Volant — vague 4
summon minecraft:vex 11.5 66 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex -11.5 66 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex 11.5 66 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex -11.5 66 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex 0.5 66 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex 0.5 66 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex 11.5 66 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex -11.5 66 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:phantom 11.5 68 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom -11.5 68 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom 11.5 68 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:phantom -11.5 68 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"8× Vex, 4× Phantom","color":"yellow"},{"text":"  (12 monstres)","color":"dark_gray"}]
