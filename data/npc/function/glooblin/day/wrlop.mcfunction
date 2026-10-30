execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wrlop","color":"light_purple"},{"text":"> Have you visited any of the three","color":"white"},{"text":" Great Forges ","color":"red"},{"text":"in the Dark Isles? Each is tended by a good-natured giant. I'm only asking because last night I had a dream that ","color":"white"},{"text":"agents of a weirding darkness","color":"red"},{"text":" were muzzling the forges' power, weakening them.","color":"white"}]

#execute at @e[sort=nearest,limit=1,tag=npc] positioned ~ ~1 ~ run tellraw @a[distance=..10] [{"text":"<"},{"text":"Wrlop","color":"light_purple"},{"text":"> The glow off the mushrooms at dusk is beautiful.","color":"white"},{"text":" Moldsap","color":"light_purple"},{"text":" is such a wonderful place to call home.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
