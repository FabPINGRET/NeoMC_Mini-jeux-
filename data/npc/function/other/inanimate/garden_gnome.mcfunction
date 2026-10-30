execute positioned 10509 57 113 run playsound minecraft:item.armor.equip_iron neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute if score mr_nippy bool matches 0 positioned 10509 57 113 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Garden Gnome","color":"red"},{"text":"> ","color":"white"},{"text":"...\nThanks for acknowledging me. As something whose entire job is to stand and look pretty, you've made me feel like I'm doing it well.","color":"gray","italic":true}]

execute if score mr_nippy bool matches 1 positioned 10509 57 113 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Garden Gnome","color":"red"},{"text":"> ","color":"white"},{"text":"...\nI'm... invited? To a thing? I'm going!","color":"gray","italic":true}]
execute if score mr_nippy bool matches 1 run setblock 10510 50 114 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
