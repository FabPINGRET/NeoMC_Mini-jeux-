execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.panda.cant_breed neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute if block 79 38 311 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless items entity @p[tag=mg.flw] weapon.mainhand minecraft:iron_sword run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ninzimrai","color":"gold"},{"text":"> You're the Hero! The ","color":"white"},{"text":"Viceroy ","color":"gold"},{"text":"has been talking for ages about how he wants to present you with a","color":"white"},{"text":" special gift","color":"gold"},{"text":". I know you want to see the ","color":"white"},{"text":"Worldgate ","color":"dark_purple"},{"text":"inside this house, but I couldn't in good conscience let you leave without making sure you'd received it first. Just show it to me when you get it, and I'll be happy to let you in.","color":"white"}]

execute if block 79 38 311 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if items entity @p[tag=mg.flw] weapon.mainhand minecraft:iron_sword run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ninzimrai","color":"gold"},{"text":"> Great, you got the ","color":"white"},{"text":"Viceroy's gift","color":"gold"},{"text":"! I hope it helps you with whatever you find in there. I've just opened the door for you.","color":"white"}]

execute unless block 79 38 311 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ninzimrai","color":"gold"},{"text":"> The door is open for you! Be careful with whatever you find on the other side.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if items entity @p[tag=mg.flw] weapon.mainhand minecraft:iron_sword run setblock 79 38 311 minecraft:redstone_torch

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
