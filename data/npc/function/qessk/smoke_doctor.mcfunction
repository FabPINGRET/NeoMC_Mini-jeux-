execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.blaze.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute if score Inventory Smokewings matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Smoke Doctor","color":"yellow"},{"text":"> Monsters, Contagions, all were pouring forth from the ","color":"white"},{"text":"Allgrave","color":"yellow"},{"text":", so I locked it with the ","color":"white"},{"text":"Lord of Smoke ","color":"yellow"},{"text":"still inside. Spirits forgive me, I locked the door through which the peaceful dead pass! If you mean to unlock the ","color":"white"},{"text":"Allgrave ","color":"yellow"},{"text":"and enter, speak with my ","color":"white"},{"text":"Igor ","color":"green"},{"text":"upstairs. Have mercy, you will understand in time why I had to seal this door so tightly. A despairing","color":"white"},{"text":" secret","color":"yellow"},{"text":"...","color":"white"}]


execute if score Inventory Smokewings matches 1 if score lord_of_valor Story matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Smoke Doctor","color":"yellow"},{"text":"> You've returned with your life, which means the ","color":"white"},{"text":"Lord of Smoke ","color":"yellow"},{"text":"is dead. He was a friend, once. The other six Lords will need to know about this...","color":"white"}]

execute if score Inventory Smokewings matches 1 if score lord_of_valor Story matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Smoke Doctor","color":"yellow"},{"text":"> I could never be a Lord, no. I am too fond of my laboratory work here. Thank you for coming to me with the offer, but no.","color":"white"}]

execute if score Inventory Smokewings matches 1 if score lord_of_valor Story matches 2.. at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Smoke Doctor","color":"yellow"},{"text":"> The ","color":"white"},{"text":"Lord of Smoke ","color":"yellow"},{"text":"was a friend, once. It took too long to let myself acknowledge his treason.","color":"white"}]

scoreboard players set can_planet bool 1

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run kill @n[tag=quest_marker,distance=..3]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
