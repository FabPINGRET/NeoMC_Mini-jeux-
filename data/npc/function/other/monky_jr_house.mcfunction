execute positioned -157 50 -234 run playsound minecraft:entity.fox.screech neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute unless block -157 50 -234 air positioned -157 50 -234 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Monky Jr.","color":"dark_green"},{"text":"> OOO EEEH EEEH! (Hey there ol' buddy ol' pal! You trying to get into ","color":"white"},{"text":"Dwarf City","color":"dark_aqua"},{"text":"? I do know of one secret way in, but it's a difficult path, full of danger and shrouded in mystery. If you really want to brave the solitary, perilous road into the city, meet me in ","color":"white"},{"text":"Monky the Bum's cave","color":"dark_green"},{"text":". Prepare well, hero!)","color":"white"}]
execute if block -157 50 -234 air positioned -157 50 -234 run tellraw @a[distance=..10,tag=mg.flw] {"text":"He's not here right now...","color":"gray","italic":true}

setblock -157 45 -234 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
