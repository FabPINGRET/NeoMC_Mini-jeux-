# Ombre d'avertissement (@s = marqueur au sol)
scoreboard players remove @s mg.t 1
particle minecraft:smoke ~ ~0.2 ~ 0.35 0 0.35 0.01 2
execute if score @s mg.t matches ..0 run function mg:anvil/shadow_end
