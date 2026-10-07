# Vie d'un mouton explosif (@s = mouton, à sa position)
# En vol : il chevauche le bloc porteur. À l'impact, le bloc disparaît,
# le mouton se pose → mèche de 1,5 s → effet (BOUM, ou effet spécial selon son type).
scoreboard players remove @s mg.t 1
particle minecraft:smoke ~ ~0.5 ~ 0.2 0.2 0.2 0.01 3

# Au sol (après l'impact) → mèche de 1,5 s (le temps de fuir !), grésillement + étincelles
execute if score @s mg.t matches 31.. unless entity @s[tag=mg.k_super] unless entity @s[tag=mg.k_ultra] unless entity @s[tag=mg.k_mitra] if data entity @s {OnGround:1b} run scoreboard players set @s mg.t 30
# Super explosif : explose DÈS l'atterrissage ; ULTRA : mèche de 2,5 s ; Mitraillette : 3 explosions espacées de 0,3 s
execute if score @s mg.t matches 1.. if entity @s[tag=mg.k_super] if data entity @s {OnGround:1b} run scoreboard players set @s mg.t 0
execute if score @s mg.t matches 51.. if entity @s[tag=mg.k_ultra] if data entity @s {OnGround:1b} run scoreboard players set @s mg.t 50
execute if score @s mg.t matches 50 if entity @s[tag=mg.k_ultra] run playsound minecraft:entity.creeper.primed master @a ~ ~ ~ 1.5 0.7
execute if score @s mg.t matches 12 if entity @s[tag=mg.k_ultra] run playsound minecraft:entity.creeper.primed master @a ~ ~ ~ 1.5 1.6
execute if score @s mg.t matches 14.. unless entity @s[tag=mg.k_super] unless entity @s[tag=mg.k_ultra] if entity @s[tag=mg.k_mitra] if data entity @s {OnGround:1b} run scoreboard players set @s mg.t 13
execute if score @s mg.t matches 12 if entity @s[tag=mg.k_mitra] run function mg:sheepwar/boom_mitra_step
execute if score @s mg.t matches 6 if entity @s[tag=mg.k_mitra] run function mg:sheepwar/boom_mitra_step
execute if score @s mg.t matches 30..49 if entity @s[tag=mg.k_ultra] run function mg:sheepwar/fuse_fx
execute if score @s mg.t matches 30 run playsound minecraft:entity.creeper.primed master @a ~ ~ ~ 1.2 1
execute if score @s mg.t matches 15 run playsound minecraft:entity.creeper.primed master @a ~ ~ ~ 1.2 1.4
execute if score @s mg.t matches 1..29 run function mg:sheepwar/fuse_fx

# Mouton de l'espace : les joueurs proches décollent 1 s avant l'explosion
execute if score @s mg.t matches 15 if entity @s[tag=mg.k_space] run effect give @a[tag=mg.play,distance=..7] minecraft:levitation 1 1 true

# Tombé dans le vide → disparaît sans effet
execute at @s if entity @s[y=-1993,dy=2048] run return run kill @s

# Fin de mèche
execute if score @s mg.t matches ..0 run function mg:sheepwar/boom
