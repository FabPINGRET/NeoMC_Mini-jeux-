execute unless score ta_lab_step Value matches 2 run scoreboard players set ta_lab_step Value 0
execute if block -11721 217 289 minecraft:redstone_lamp[lit=false] run scoreboard players set ta_lab_step Value 0
execute if score ta_lab_step Value matches 2 run scoreboard players add ta_lab_pumps Value 1


scoreboard players set ta_lab_kablasts Value 0
scoreboard players set ta_lab_safe_next_fluid Value 0
scoreboard players set ta_lab_fluid_a_injects Value 0
