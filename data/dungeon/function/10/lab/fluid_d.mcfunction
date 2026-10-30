execute unless score ta_lab_safe_next_fluid Value matches 4 run scoreboard players set ta_lab_step Value 0
execute if score ta_lab_step Value matches 4 if score ta_lab_safe_next_fluid Value matches 4 if block -11711 218 306 minecraft:ochre_froglight if block -11711 218 307 minecraft:ochre_froglight if block -11711 218 308 minecraft:ochre_froglight run function dungeon:10/lab/proceed/5


scoreboard players set ta_lab_kablasts Value 0
scoreboard players set ta_lab_pumps Value 0

scoreboard players set ta_lab_fluid_a_injects Value 0
