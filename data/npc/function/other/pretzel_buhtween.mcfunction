execute positioned 9096 178 -1017 run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2


execute positioned 9096 178 -1017 run tellraw @a[distance=..10,tag=!vendor_pretzel,tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> Here's today's item from ","color":"white"},{"text":"The Inviolable Barrel of One Billion Crud","color":"red"},{"text":"! Haha, I hope you like it! Come back tomorrow and I'll give you another ","color":"white"},{"text":"random object ","color":"red"},{"text":"from its barrel hole.","color":"white"}]

execute positioned 9096 178 -1017 run tellraw @a[distance=..10,tag=vendor_pretzel,tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> Haha! I can see you! Yes, ","color":"white"},{"selector":"@p[tag=mg.flw]","separator":""},{"text":", I can see you in a room looking at a screen! Haha! Your secret's safe with me...","color":"white"}]


execute positioned 9096 178 -1017 as @a[distance=..10,tag=!vendor_pretzel,tag=mg.flw] run function game:pretzel_item
execute positioned 9096 178 -1017 run tag @a[distance=..10,tag=!vendor_pretzel,tag=mg.flw] add vendor_pretzel



#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
