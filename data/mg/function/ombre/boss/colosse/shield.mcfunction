# Le Colosse de runes : shield
execute if entity @e[tag=mg.olpill,scores={mg.olst=..0}] run return run data merge entity @s {Invulnerable:1b,Glowing:1b}
execute if entity @s[nbt={Invulnerable:1b}] run tellraw @a[distance=..40] {"text":"Les quatre piliers sont éteints : le Colosse est vulnérable !","color":"aqua","bold":true}
data merge entity @s {Invulnerable:0b,Glowing:0b}
