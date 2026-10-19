# @s : bonus du niveau (+1 PV par niveau), des caractéristiques et de la classe
attribute @s minecraft:max_health modifier remove mg:ollv
execute store result storage mg:ombre st.lv int 1 run scoreboard players get @s mg.ollv
execute store result storage mg:ombre st.v float 2 run scoreboard players get @s mg.ols1
execute store result storage mg:ombre st.f float 0.5 run scoreboard players get @s mg.ols2
execute store result storage mg:ombre st.a float 0.015 run scoreboard players get @s mg.ols3
function mg:ombre/stats_m with storage mg:ombre st
function mg:ombre/cl/passive
function mg:ombre/mana_max
