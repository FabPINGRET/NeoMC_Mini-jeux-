# Volant — vague 2
summon minecraft:vex 11.5 66 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex -11.5 66 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex 11.5 66 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex -11.5 66 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex 0.5 66 1811.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
summon minecraft:vex 0.5 66 1789.5 {Tags:["mg.mob"],PersistenceRequired:1b,equipment:{mainhand:{id:"minecraft:iron_sword",count:1}}}
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"6× Vex","color":"yellow"},{"text":"  (6 monstres)","color":"dark_gray"}]
