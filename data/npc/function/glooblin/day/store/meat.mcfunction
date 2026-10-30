execute if score Inventory DayNight matches 2 positioned 10376 57 -193 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"Phmlub the shopkeeper isn't here right now. Don't steal.","color":"gray","italic":true}]

execute if score Inventory DayNight matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if score BetterEconomy bool matches 0 if score Inventory DayNight matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Phmlub","color":"light_purple"},{"text":"> The economy is in the toilet right now, so I don't have any, um, Mete for you. Sorry.","color":"white"}]
execute if score BetterEconomy bool matches 1 if score Inventory DayNight matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_cooked_beef_1,tag=mg.flw] [{"text":"<"},{"text":"Phmlub","color":"light_purple"},{"text":"> That's called Mete! Take some steaks.","color":"white"}]
execute if score BetterEconomy bool matches 1 if score Inventory DayNight matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_cooked_beef_1,tag=mg.flw] [{"text":"<"},{"text":"Phmlub","color":"light_purple"},{"text":"> I don't think I have the inventory for you to take more right now. Come back tomorrow!","color":"white"}]

execute if score BetterEconomy bool matches 1 if score Inventory DayNight matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_cooked_beef_1,tag=mg.flw] cooked_beef 16
execute if score BetterEconomy bool matches 1 if score Inventory DayNight matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_cooked_beef_1,tag=mg.flw] add vendor_cooked_beef_1

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
