# Splegg — début de partie
gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run function mg:splegg/give_all
tellraw @a[tag=mg.play] [{"text":"❍ SPLEGG ! Clic droit pour tirer des œufs : ils détruisent la neige là où ils touchent. Fais tomber les autres dans le vide — dernier debout = gagnant !","color":"yellow"}]
tellraw @a[tag=mg.play] [{"text":"(munitions infinies — tu peux tirer à volonté)","color":"dark_gray","italic":true}]
execute if score $sg mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"XXL : 3 étages géants, chaque œuf détruit 3x3 blocs !","color":"gold"}]

execute unless score $sg mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"3 étages : troue la neige pour faire tomber les autres… ou descends-les toi-même !","color":"gold"}]
scoreboard players set $tff mg.st 0
