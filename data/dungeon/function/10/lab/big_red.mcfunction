execute if score ta_lab_step Value matches 8 run setblock -11713 227 310 minecraft:redstone_block

scoreboard players set ta_lab_kablasts Value 0
scoreboard players set ta_lab_pumps Value 0
#0 is none, 1 is A, 2 is B, etc.
scoreboard players set ta_lab_safe_next_fluid Value 0
scoreboard players set ta_lab_fluid_a_injects Value 0

scoreboard players set ta_lab_a_results Value 0
scoreboard players set ta_lab_b_results Value 0

execute store result score ta_lab_a_results Value run random value 3..5
execute store result score ta_lab_b_results Value run random value 1..3

data merge block -11710 218 294 {front_text:{messages:["Virometer:","",{"text":"x","color":"dark_aqua","bold":true,"obfuscated":true},""]}}

execute if block -11721 217 289 redstone_lamp[lit=false] if blocks -11711 218 306 -11711 218 308 -11711 220 306 all run function dungeon:10/lab/proceed/1
