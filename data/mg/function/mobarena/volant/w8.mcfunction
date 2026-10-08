# Volant — vague 8
summon minecraft:vex 11.5 66 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex -11.5 66 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex 11.5 66 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex -11.5 66 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex 0.5 66 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex 0.5 66 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex 11.5 66 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex -11.5 66 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex 11.5 66 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex -11.5 66 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:blaze 11.5 65 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze -11.5 65 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze 0.5 65 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze 0.5 65 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:blaze 11.5 65 1800.5 {Tags:["mg.mob"],PersistenceRequired:1b}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"10× Vex, 5× Blaze","color":"yellow"},{"text":"  (15 monstres)","color":"dark_gray"}]
