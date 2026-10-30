execute if score golem_lycan bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.ravager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute if score golem_lycan bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.breeze.deflect neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score golem_lycan bool matches 0 if score moonlight_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mogrod","color":"red"},{"text":"> The monsters that appear at night in the ","color":"white"},{"text":"Magma Kingdom ","color":"red"},{"text":"are stronger than almost anywhere else in the Isles. Be careful here, hero.","color":"white"}]
execute if score golem_lycan bool matches 0 if score moonlight_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mogrod","color":"red"},{"text":"> Maybe the Sun and Moon both have a part to play in our theology now. The Moon answers our prayers of becoming alive, and the Sun burns away the monsters of the night!","color":"white"}]

execute if score golem_lycan bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mogrodox","color":"red"},{"text":"> Cheep, cheep! Haha, I just wanted to see how that would feel to say!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
