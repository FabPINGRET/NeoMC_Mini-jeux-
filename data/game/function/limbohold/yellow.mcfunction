tag @s remove lh_v_1
tag @s remove lh_v_2
tag @s remove lh_v_3
tag @s remove lh_v_4
tag @s remove lh_v_5
tag @s remove lh_v_6
tag @s remove lh_v_7
tag @s remove lh_v_8
tag @s remove lh_v_9
tag @s remove lh_v_12
execute if entity @s[tag=lh_v_11] run tag @s add lh_v_12
tag @s remove lh_v_11
execute if entity @s[tag=lh_v_10] run tag @s add lh_v_11
tag @s remove lh_v_10

tag @s remove lh_r_4
execute if entity @s[tag=lh_r_3] run tag @s add lh_r_4
tag @s remove lh_r_1
tag @s remove lh_r_2
tag @s remove lh_r_3


tag @s remove lh_s_4
execute if entity @s[tag=lh_s_3] run tag @s add lh_s_4
execute if entity @s[tag=lh_s_2] run tag @s add lh_s_3
execute if entity @s[tag=lh_s_1] run tag @s add lh_s_2
tag @s add lh_s_1

tag @s remove lh_l_4
execute if entity @s[tag=lh_l_3] run tag @s add lh_l_4

tag @s remove lh_l_1
tag @s remove lh_l_2
tag @s remove lh_l_3

#Alabaster
tag @s remove lh_a_1
tag @s remove lh_a_2
tag @s remove lh_a_3
tag @s remove lh_a_7
tag @s remove lh_a_8
tag @s remove lh_a_9
tag @s remove lh_a_11
tag @s remove lh_a_13
tag @s remove lh_a_15
tag @s remove lh_a_16
execute if entity @s[tag=lh_a_14] run tag @s add lh_a_15
tag @s remove lh_a_14
execute if entity @s[tag=lh_a_12] run tag @s add lh_a_13
tag @s remove lh_a_12
execute if entity @s[tag=lh_a_10] run tag @s add lh_a_11
tag @s remove lh_a_10
execute if entity @s[tag=lh_a_6] run tag @s add lh_a_7
tag @s remove lh_a_6
execute if entity @s[tag=lh_a_5] run tag @s add lh_a_6
tag @s remove lh_a_5
execute if entity @s[tag=lh_a_4] run tag @s add lh_a_5
tag @s remove lh_a_4

#Funeral Chapel
tag @s remove lh_f_1
tag @s remove lh_f_2
tag @s remove lh_f_3
tag @s remove lh_f_4
tag @s remove lh_f_5
tag @s remove lh_f_6
tag @s remove lh_f_7
tag @s remove lh_f_9
tag @s remove lh_f_10
tag @s remove lh_f_11
tag @s remove lh_f_13
tag @s remove lh_f_15
execute if entity @s[tag=lh_f_12] run tag @s add lh_f_13
tag @s remove lh_f_12
execute if entity @s[tag=lh_f_8] run tag @s add lh_f_9
tag @s remove lh_f_8
execute if entity @s[tag=lh_f_14] run tag @s add lh_f_15
tag @s remove lh_f_14

execute if entity @s[tag=lh_s_4] run tp @s ~-3 ~-8 ~124
execute if entity @s[tag=lh_v_12] run tp @s ~-6 ~-5 ~54
execute if entity @s[tag=lh_f_15] run tp @s ~-45 ~-5 ~54
execute unless entity @s[tag=lh_v_12] unless entity @s[tag=lh_s_4] unless entity @s[tag=lh_f_15] run tp @s ~ ~ ~-8

#unless entity @s[tag=lh_r_4]
