execute if block 79 35 -122 air unless score Inventory Time matches 1 positioned 79 35 -122 run tellraw @a[distance=..20,tag=mg.flw] {"text":"Not now, but... During sunrise... Yes, do that again during sunrise... That would feel... good...","italic":true,"color":"red"}
execute if block 79 35 -122 air if score Inventory Time matches 1 positioned 79 35 -122 run tellraw @a[distance=..20,tag=mg.flw] {"text":"Ah... That feels... good... Thank you...","italic":true,"color":"red"}
execute if block 79 35 -122 air if score Inventory Time matches 1 positioned 79 35 -122 run setblock 64 39 -128 minecraft:redstone_block

execute unless block 79 35 -122 air positioned 79 35 -122 run tellraw @a[distance=..20,tag=mg.flw] {"text":"Ah... One arrow is... enough... Thanks though...","italic":true,"color":"red"}


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
