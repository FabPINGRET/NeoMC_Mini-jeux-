execute unless score ta_lab_safe_next_fluid Value matches 1 run scoreboard players set ta_lab_step Value 0
execute if score ta_lab_step Value matches 1 if score ta_lab_safe_next_fluid Value matches 1 run scoreboard players set ta_lab_safe_next_fluid Value 3
execute if score ta_lab_step Value matches 5 if score ta_lab_safe_next_fluid Value matches 1 run scoreboard players add ta_lab_fluid_a_injects Value 1

scoreboard players set ta_lab_kablasts Value 0
scoreboard players set ta_lab_pumps Value 0
