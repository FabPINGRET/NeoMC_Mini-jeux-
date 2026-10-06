# Sheep War — lancement d'un mouton (@s = joueur, exécuté aux yeux)
# Le mouton surfe sur un BLOC DE LAINE TOMBANT : vraie balistique, aucune collision
# avec les entités (contrairement à un projectile), et il explose À L'ARRIVÉE.

# Marqueurs pour calculer le vecteur de visée (vitesse ≈ 2.5 blocs/tick)
summon minecraft:marker ^ ^ ^0 {Tags:["mg.m0"]}
summon minecraft:marker ^ ^ ^2.5 {Tags:["mg.m1"]}

# Bloc de laine porteur + mouton passager (couleur d'équipe)
execute if entity @s[team=mg_red] run summon minecraft:falling_block ^ ^ ^1.2 {Tags:["mg.proj","mg.newp"],Time:1,DropItem:0b,CancelDrop:1b,BlockState:{Name:"minecraft:red_wool"},Passengers:[{id:"minecraft:sheep",Color:14b,Tags:["mg.sheep","mg.news"],PersistenceRequired:1b,Invulnerable:1b,attributes:[{id:"minecraft:explosion_knockback_resistance",base:1.0d}],CustomName:[{"text":"BÊÊÊ","color":"red"}]}]}
execute if entity @s[team=mg_blue] run summon minecraft:falling_block ^ ^ ^1.2 {Tags:["mg.proj","mg.newp"],Time:1,DropItem:0b,CancelDrop:1b,BlockState:{Name:"minecraft:blue_wool"},Passengers:[{id:"minecraft:sheep",Color:11b,Tags:["mg.sheep","mg.news"],PersistenceRequired:1b,Invulnerable:1b,attributes:[{id:"minecraft:explosion_knockback_resistance",base:1.0d}],CustomName:[{"text":"BÊÊÊ","color":"blue"}]}]}

# Vecteur (m1 - m0), échelle ×1000
execute store result score $x1 mg.st run data get entity @e[tag=mg.m1,limit=1] Pos[0] 1000
execute store result score $y1 mg.st run data get entity @e[tag=mg.m1,limit=1] Pos[1] 1000
execute store result score $z1 mg.st run data get entity @e[tag=mg.m1,limit=1] Pos[2] 1000
execute store result score $x0 mg.st run data get entity @e[tag=mg.m0,limit=1] Pos[0] 1000
execute store result score $y0 mg.st run data get entity @e[tag=mg.m0,limit=1] Pos[1] 1000
execute store result score $z0 mg.st run data get entity @e[tag=mg.m0,limit=1] Pos[2] 1000
scoreboard players operation $x1 mg.st -= $x0 mg.st
scoreboard players operation $y1 mg.st -= $y0 mg.st
scoreboard players operation $z1 mg.st -= $z0 mg.st

# → storage en doubles
execute store result storage mg:v x double 0.001 run scoreboard players get $x1 mg.st
execute store result storage mg:v y double 0.001 run scoreboard players get $y1 mg.st
execute store result storage mg:v z double 0.001 run scoreboard players get $z1 mg.st

kill @e[tag=mg.m0]
kill @e[tag=mg.m1]

# Mouton spécial (item dédié) : apparence et type selon $ty
execute if score $ty mg.st matches 1.. as @e[tag=mg.news,limit=1] run function mg:sheepwar/special_set

# Applique la vitesse à la boule porteuse + mèche de vol (8 s max, mèche de 1,5 s après l'atterrissage)
execute as @e[tag=mg.newp,limit=1] run function mg:sheepwar/motion with storage mg:v
tag @e[tag=mg.newp] remove mg.newp
scoreboard players set @e[tag=mg.news,limit=1] mg.t 160
tag @e[tag=mg.news] remove mg.news

execute at @s run playsound minecraft:entity.sheep.ambient master @a ~ ~ ~ 1 1.3
execute at @s run playsound minecraft:entity.firework_rocket.launch master @a ~ ~ ~ 0.8 0.9
