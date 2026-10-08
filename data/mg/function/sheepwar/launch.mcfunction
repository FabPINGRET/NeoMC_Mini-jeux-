# Sheep War — lancement d'un mouton (@s = joueur, exécuté aux yeux)
# Le mouton vole seul, déplacé par le serveur à chaque tick (sheepwar/fly) : balistique d'un bloc tombant
# (gravité 0,04, frottement 0,98), aucune collision avec les entités, et il explose À L'ARRIVÉE.
# (L'ancien bloc de laine porteur n'était resynchronisé chez les joueurs qu'une fois par seconde :
#  le mouton semblait se téléporter ailleurs que là où on visait.)

# Marqueurs pour calculer le vecteur de visée (vitesse ≈ 2.5 blocs/tick)
summon minecraft:marker ^ ^ ^0 {Tags:["mg.m0"]}
summon minecraft:marker ^ ^ ^2.5 {Tags:["mg.m1"]}

# Mouton volant (couleur d'équipe)
execute if entity @s[team=mg_red] run summon minecraft:sheep ^ ^ ^1.2 {Color:14b,Tags:["mg.sheep","mg.news","mg.fly"],NoGravity:1b,NoAI:1b,PersistenceRequired:1b,Invulnerable:1b,attributes:[{id:"minecraft:explosion_knockback_resistance",base:1.0d}],CustomName:[{"text":"BÊÊÊ","color":"red"}]}
execute if entity @s[team=mg_blue] run summon minecraft:sheep ^ ^ ^1.2 {Color:11b,Tags:["mg.sheep","mg.news","mg.fly"],NoGravity:1b,NoAI:1b,PersistenceRequired:1b,Invulnerable:1b,attributes:[{id:"minecraft:explosion_knockback_resistance",base:1.0d}],CustomName:[{"text":"BÊÊÊ","color":"blue"}]}

# Vecteur (m1 - m0), échelle ×1000
execute store result score $x1 mg.st run data get entity @e[tag=mg.m1,limit=1,sort=nearest] Pos[0] 1000
execute store result score $y1 mg.st run data get entity @e[tag=mg.m1,limit=1,sort=nearest] Pos[1] 1000
execute store result score $z1 mg.st run data get entity @e[tag=mg.m1,limit=1,sort=nearest] Pos[2] 1000
execute store result score $x0 mg.st run data get entity @e[tag=mg.m0,limit=1,sort=nearest] Pos[0] 1000
execute store result score $y0 mg.st run data get entity @e[tag=mg.m0,limit=1,sort=nearest] Pos[1] 1000
execute store result score $z0 mg.st run data get entity @e[tag=mg.m0,limit=1,sort=nearest] Pos[2] 1000
scoreboard players operation $x1 mg.st -= $x0 mg.st
scoreboard players operation $y1 mg.st -= $y0 mg.st
scoreboard players operation $z1 mg.st -= $z0 mg.st

# Vitesse du mouton (×1000) : déplacée par sheepwar/fly à chaque tick
scoreboard players operation @e[tag=mg.news,limit=1,sort=nearest] mg.svx = $x1 mg.st
scoreboard players operation @e[tag=mg.news,limit=1,sort=nearest] mg.svy = $y1 mg.st
scoreboard players operation @e[tag=mg.news,limit=1,sort=nearest] mg.svz = $z1 mg.st

kill @e[tag=mg.m0]
kill @e[tag=mg.m1]

# Mouton spécial (item dédié) : apparence et type selon $ty
execute if score $ty mg.st matches 1.. as @e[tag=mg.news,limit=1,sort=nearest] run function mg:sheepwar/special_set

# Durée de vol maximale 8 s (mèche de 1,5 s après l'atterrissage)
scoreboard players set @e[tag=mg.news,limit=1] mg.t 160
tag @e[tag=mg.news] remove mg.news

execute at @s run playsound minecraft:entity.sheep.ambient master @a ~ ~ ~ 1 1.3
execute at @s run playsound minecraft:entity.firework_rocket.launch master @a ~ ~ ~ 0.8 0.9
