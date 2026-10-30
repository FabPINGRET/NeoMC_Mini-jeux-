execute if score golem_lycan bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.ravager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute if score golem_lycan bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.breeze.deflect neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score golem_lycan bool matches 0 if score moonlight_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_baked_potato_0,tag=mg.flw] [{"text":"<"},{"text":"Ogrock","color":"red"},{"text":"> You ever had a tater baked over lava? You gotta tell me how they are! I am made of rocks and thus unable to taste.","color":"white"}]
execute if score golem_lycan bool matches 0 if score moonlight_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_baked_potato_0,tag=mg.flw] [{"text":"<"},{"text":"Ogrock","color":"red"},{"text":"> I don't have any more taters for you, sorry. I know I'm holding one in my hand but it's for me. I'm gonna practice trying to taste it.","color":"white"}]

execute if score golem_lycan bool matches 0 if score moonlight_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_baked_potato_0,tag=mg.flw] [{"text":"<"},{"text":"Ogrock","color":"red"},{"text":"> You ever had a tater baked over lava? I just tried them for the first time as a ","color":"white"},{"text":"Werewing","color":"red"},{"text":"! Good stuff, they are.","color":"white"}]
execute if score golem_lycan bool matches 0 if score moonlight_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_baked_potato_0,tag=mg.flw] [{"text":"<"},{"text":"Ogrock","color":"red"},{"text":"> I don't have any more taters for you, sorry. I know I'm holding one in my hand but it's for me. I'm gonna eat it tonight!","color":"white"}]

execute if score golem_lycan bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_baked_potato_0,tag=mg.flw] [{"text":"<"},{"text":"Ogrockax","color":"red"},{"text":"> You ever had a tater baked over lava? I just tried them for the first time! Good stuff, they are.","color":"white"}]
execute if score golem_lycan bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_baked_potato_0,tag=mg.flw] [{"text":"<"},{"text":"Ogrockax","color":"red"},{"text":"> I don't have any more taters for you, sorry. I know I'm holding one in my hand but it's for me. I'm gonna savor the smell for a while before I eat it!","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_baked_potato_0,tag=mg.flw] baked_potato 20
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_baked_potato_0,tag=mg.flw] add vendor_baked_potato_0


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
