execute if score golem_lycan bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.ravager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute if score golem_lycan bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.breeze.deflect neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score golem_lycan bool matches 0 if score moonlight_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bugnod","color":"red"},{"text":"> We don't need to sleep. These beds are for when","color":"white"},{"text":" Dwarves","color":"dark_aqua"},{"text":" come to visit us, which they haven't done in a while.","color":"white"}]
execute if score golem_lycan bool matches 0 if score moonlight_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bugnod","color":"red"},{"text":"> We don't need to sleep. These beds are for when ","color":"white"},{"text":"Dwarves","color":"dark_aqua"},{"text":" come to visit us, which they haven't done in a while. It's a shame the ","color":"white"},{"text":"Dwarves","color":"dark_aqua"},{"text":" can't change into something really cool at night.","color":"white"}]

execute if score golem_lycan bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bugnodex","color":"red"},{"text":"> I'm so glad we turn into avian creatures instead of something scary like wolves.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
