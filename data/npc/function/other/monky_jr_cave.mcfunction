execute positioned -108 40 -167 run playsound minecraft:entity.fox.screech neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned -108 40 -167 if entity @a[distance=..10,gamemode=!spectator,tag=mg.flw] unless entity @a[distance=10..,gamemode=!spectator,tag=mg.flw] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Monky Jr.","color":"dark_green"},{"text":"> AHH AHH OOH OOH! (You're here. I'll open the door for you, but I'll warn you, listen to everything I say when you're in this cave. It will take you inside ","color":"white"},{"text":"Dwarf City","color":"dark_aqua"},{"text":", but if you stray from my direction in any way, you could die. Best of luck, hero. I'll be waiting for you on the other side.)","color":"white"}]

execute positioned -108 40 -167 if entity @a[distance=10..,gamemode=!spectator,tag=mg.flw] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Monky Jr.","color":"dark_green"},{"text":"> AHH OOOOH EEH! (Have everyone gather in here first! You're gonna need as much help as you can get.)","color":"white"}]

execute positioned -108 40 -167 if entity @a[distance=..10,gamemode=!spectator,tag=mg.flw] unless entity @a[distance=10..,gamemode=!spectator,tag=mg.flw] run setblock -108 34 -177 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
