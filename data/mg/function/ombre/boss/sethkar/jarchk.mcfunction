# Plus de vases : Sethkar redevient vulnérable
execute if entity @e[type=minecraft:interaction,tag=mg.oljar] run return run particle minecraft:enchant ~ ~2 ~ 1 1 1 0.5 20
execute if entity @s[nbt={Invulnerable:1b}] run tellraw @a[distance=..40] {"text":"La protection de Sethkar se brise !","color":"gold"}
data merge entity @s {Invulnerable:0b}
