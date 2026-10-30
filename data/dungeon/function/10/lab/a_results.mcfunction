execute unless score ta_lab_step Value matches 2 run scoreboard players set ta_lab_step Value 0
execute if block -11721 217 289 minecraft:redstone_lamp[lit=false] run scoreboard players set ta_lab_step Value 0
data merge block -11710 218 294 {front_text:{messages:["Virometer:","",{"score":{"name":"ta_lab_a_results","objective":"Value"},"color":"dark_aqua","bold":true},""]}}

scoreboard players set ta_lab_kablasts Value 0
