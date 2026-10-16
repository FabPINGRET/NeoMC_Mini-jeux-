# @s : bonus des caractéristiques (modificateurs mg:trst*)
attribute @s minecraft:max_health modifier remove mg:trst
attribute @s minecraft:attack_damage modifier remove mg:trst
attribute @s minecraft:movement_speed modifier remove mg:trst
execute store result storage mg:terra st.v float 2 run scoreboard players get @s mg.trs1
execute store result storage mg:terra st.f float 0.5 run scoreboard players get @s mg.trs2
execute store result storage mg:terra st.a float 0.02 run scoreboard players get @s mg.trs3
function mg:terra/rpg/st/apply_m with storage mg:terra st
