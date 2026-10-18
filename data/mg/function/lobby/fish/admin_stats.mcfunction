# Admin (@s) : compteurs d'usage de la pêche (objectif mg.lfn), depuis sa création
execute unless score $rod mg.lfn matches 0.. run scoreboard players set $rod mg.lfn 0
execute unless score $catch mg.lfn matches 0.. run scoreboard players set $catch mg.lfn 0
execute unless score $gold mg.lfn matches 0.. run scoreboard players set $gold mg.lfn 0
execute unless score $junk mg.lfn matches 0.. run scoreboard players set $junk mg.lfn 0
execute unless score $use mg.lfn matches 0.. run scoreboard players set $use mg.lfn 0
# la stat vanilla compte le lancer et la remontée : lancers ≈ $use / 2
scoreboard players operation $cast mg.lfn = $use mg.lfn
scoreboard players set #lf2 mg.st 2
scoreboard players operation $cast mg.lfn /= #lf2 mg.st
execute if score $lfoff mg.st matches 1 run tellraw @s {"text":"🎣 Pêche à l'étang : désactivée","color":"red"}
execute unless score $lfoff mg.st matches 1 run tellraw @s {"text":"🎣 Pêche à l'étang : activée","color":"green"}
tellraw @s [{"text":"Usage : ","color":"gray"},{"text":"🎣 Cannes prises ","color":"white"},{"score":{"name":"$rod","objective":"mg.lfn"},"color":"yellow"},{"text":" · ⭐ Prises ","color":"white"},{"score":{"name":"$catch","objective":"mg.lfn"},"color":"yellow"},{"text":" · ✨ Dorés ","color":"white"},{"score":{"name":"$gold","objective":"mg.lfn"},"color":"yellow"},{"text":" · Déchets ","color":"white"},{"score":{"name":"$junk","objective":"mg.lfn"},"color":"yellow"},{"text":" · 🎣 Lancers ≈ ","color":"white"},{"score":{"name":"$cast","objective":"mg.lfn"},"color":"yellow"}]
