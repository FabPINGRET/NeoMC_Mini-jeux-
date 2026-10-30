execute positioned -234 41 -154 run playsound minecraft:entity.fox.screech neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned -234 41 -154 run tellraw @a[distance=..30,tag=mg.flw] [{"text":"<"},{"text":"Monky Jr.","color":"dark_green"},{"text":"> EEH AH AHHHH EEEEH! (Oh my banana, you survived! This door is my secret way into ","color":"white"},{"text":"Dwarf City","color":"dark_aqua"},{"text":", I'll open it for you now. Hm? What do you mean we could've just walked here? Next time find your own way to this door if you're gonna be ungrateful, I risked my life for you! I'm going home.)","color":"white"}]

setblock -238 38 -150 minecraft:redstone_block
setblock -231 38 -152 minecraft:redstone_torch

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
