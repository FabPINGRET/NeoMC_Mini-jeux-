execute positioned -288 58 -191 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -288 58 -191 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Yemdok","color":"dark_aqua"},{"text":"> We're supposed to be creating spaces where dwarves can relax and enjoy the natural granite, but who can relax in times like these?","color":"white"}]
execute positioned -288 58 -191 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Yemdok","color":"dark_aqua"},{"text":"> We're supposed to be creating spaces where dwarves can relax and enjoy the natural granite, but we don't get great funding to be honest with you.","color":"white"}]

setblock -9762 76 416 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
