execute unless score ta_lab_step Value matches 2 unless score ta_lab_step Value matches 3 unless score ta_lab_step Value matches 5 unless score ta_lab_step Value matches 6 run scoreboard players set ta_lab_step Value 0

execute if score ta_lab_step Value matches 3 run function dungeon:10/lab/proceed/4
execute if score ta_lab_step Value matches 2 unless score ta_lab_a_results Value = ta_lab_pumps Value run scoreboard players set ta_lab_step Value 0
execute if score ta_lab_step Value matches 2 if score ta_lab_a_results Value = ta_lab_pumps Value run function dungeon:10/lab/proceed/3

execute if score ta_lab_step Value matches 6 run function dungeon:10/lab/proceed/7
execute if score ta_lab_step Value matches 5 unless score ta_lab_b_results Value = ta_lab_fluid_a_injects Value run scoreboard players set ta_lab_step Value 0
execute if score ta_lab_step Value matches 5 if score ta_lab_b_results Value = ta_lab_fluid_a_injects Value run function dungeon:10/lab/proceed/6
