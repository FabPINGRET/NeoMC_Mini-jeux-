execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.witch.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute if score Inventory Smokewings matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Igor","color":"yellow"},{"text":"> ","color":"white"},{"text":"The door to the","color":"white"},{"text":" Allgrave ","color":"yellow"},{"text":"is closssed, even to the dead. The Smoke Doctor sealed it with ","color":"white"},{"text":"four keys","color":"yellow"},{"text":", and put each key into a ","color":"white"},{"text":"tiny planet","color":"green"},{"text":". Each planet was given to a ruler in the ","color":"white"},{"text":"Floaty Islesss ","color":"gold"},{"text":"as a gift for them to safeguard. One to a king, one to a captain, one to a viceroy and one to a czar. To recover the keys, you would need to visit the planetsss...","color":"white"}]

execute if score Inventory Smokewings matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Igor","color":"yellow"},{"text":"> ","color":"white"},{"text":"You've sssolved one problem but causssed another. Our Lord is dead becaussse of you. What a disgusssting turn of eventsss.","color":"white"}]

scoreboard players set can_planet bool 1

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run kill @n[tag=quest_marker,distance=..3]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
