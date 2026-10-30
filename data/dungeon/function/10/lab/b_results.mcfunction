execute unless score ta_lab_step Value matches 5 run scoreboard players set ta_lab_step Value 0
execute if score ta_lab_step Value matches 5 if score ta_lab_safe_next_fluid Value matches 0 run scoreboard players set ta_lab_safe_next_fluid Value 1

data merge block -11710 218 294 {front_text:{messages:["Virometer:","",{"score":{"name":"ta_lab_b_results","objective":"Value"},"color":"dark_aqua","bold":true},""]}}

scoreboard players set ta_lab_kablasts Value 0
scoreboard players set ta_lab_pumps Value 0
scoreboard players set ta_lab_fluid_a_injects Value 0
