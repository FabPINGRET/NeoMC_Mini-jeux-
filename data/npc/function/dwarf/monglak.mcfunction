execute positioned -215 59 -101 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -215 59 -101 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Monglak","color":"dark_aqua"},{"text":"> I'm pretty confident no one in the Dwarf Legion is secretly a bone monster. If anything, we're muscle monsters HAH! On account of that we're so strong. Me anyway. I am anyway, I mean.","color":"white"}]
execute positioned -215 59 -101 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Monglak","color":"dark_aqua"},{"text":"> No one in the Dwarf Legion was a bone monster! We're all muscle monsters though HAH! On account of that we're so strong. Me anyway. I am anyway, I mean.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
