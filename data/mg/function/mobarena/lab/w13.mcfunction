# Laboratoire — vague 13
summon minecraft:zombie 14.5 65 9500.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:glass",count:1},chest:{id:"minecraft:leather_chestplate",count:1},mainhand:{id:"minecraft:iron_shovel",count:1}}}
summon minecraft:zombie -13.5 65 9500.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:glass",count:1},chest:{id:"minecraft:leather_chestplate",count:1},mainhand:{id:"minecraft:iron_shovel",count:1}}}
summon minecraft:zombie 0.5 65 9514.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:glass",count:1},chest:{id:"minecraft:leather_chestplate",count:1},mainhand:{id:"minecraft:iron_shovel",count:1}}}
summon minecraft:zombie 0.5 65 9486.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:glass",count:1},chest:{id:"minecraft:leather_chestplate",count:1},mainhand:{id:"minecraft:iron_shovel",count:1}}}
summon minecraft:zombie 10.5 65 9510.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:glass",count:1},chest:{id:"minecraft:leather_chestplate",count:1},mainhand:{id:"minecraft:iron_shovel",count:1}}}
summon minecraft:zombie -9.5 65 9510.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:glass",count:1},chest:{id:"minecraft:leather_chestplate",count:1},mainhand:{id:"minecraft:iron_shovel",count:1}}}
summon minecraft:zombie 10.5 65 9490.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:glass",count:1},chest:{id:"minecraft:leather_chestplate",count:1},mainhand:{id:"minecraft:iron_shovel",count:1}}}
summon minecraft:zombie -9.5 65 9490.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:glass",count:1},chest:{id:"minecraft:leather_chestplate",count:1},mainhand:{id:"minecraft:iron_shovel",count:1}}}
summon minecraft:zombie 14.5 65 9507.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:glass",count:1},chest:{id:"minecraft:leather_chestplate",count:1},mainhand:{id:"minecraft:iron_shovel",count:1}}}
summon minecraft:zombie -13.5 65 9507.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:glass",count:1},chest:{id:"minecraft:leather_chestplate",count:1},mainhand:{id:"minecraft:iron_shovel",count:1}}}
summon minecraft:zombie 14.5 65 9493.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:glass",count:1},chest:{id:"minecraft:leather_chestplate",count:1},mainhand:{id:"minecraft:iron_shovel",count:1}}}
summon minecraft:zombie -13.5 65 9493.5 {Tags:["mg.mob","mg.fz"],PersistenceRequired:1b,equipment:{head:{id:"minecraft:glass",count:1},chest:{id:"minecraft:leather_chestplate",count:1},mainhand:{id:"minecraft:iron_shovel",count:1}}}
summon minecraft:witch 7.5 65 9514.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:witch -6.5 65 9514.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:witch 7.5 65 9486.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:witch -6.5 65 9486.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:witch 14.5 65 9500.5 {Tags:["mg.mob"],PersistenceRequired:1b}
summon minecraft:creeper -13.5 65 9500.5 {Tags:["mg.mob"],PersistenceRequired:1b,powered:1b}
summon minecraft:creeper 0.5 65 9514.5 {Tags:["mg.mob"],PersistenceRequired:1b,powered:1b}
summon minecraft:creeper 0.5 65 9486.5 {Tags:["mg.mob"],PersistenceRequired:1b,powered:1b}
summon minecraft:creeper 10.5 65 9510.5 {Tags:["mg.mob"],PersistenceRequired:1b,powered:1b}
effect give @e[tag=mg.fz] minecraft:speed infinite 1 true
tag @e[tag=mg.fz] remove mg.fz
execute unless score $wdup mg.st matches 1 run tellraw @a [{"text":"  ➜ ","color":"gray"},{"text":"12× Zombie de laboratoire (Speed II), 5× Sorcière, 4× Creeper chargé","color":"yellow"},{"text":"  (21 monstres)","color":"dark_gray"}]
