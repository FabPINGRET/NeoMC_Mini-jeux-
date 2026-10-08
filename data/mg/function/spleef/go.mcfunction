# Spleef — début de partie
gamemode survival @a[tag=mg.play]
give @a[tag=mg.play] minecraft:diamond_shovel[unbreakable={},enchantments={efficiency:5},custom_name=[{"text":"Pelle à Spleef","color":"aqua","italic":false}]]
scoreboard players set $sk mg.st 800
scoreboard players set $ss mg.st 0
tellraw @a[tag=mg.play] [{"text":"❄ Casse la neige sous les pieds des autres ! Dernier debout = gagnant. Attention : au bout de 40 s, l'arène rétrécit...","color":"aqua"}]
execute if score $nf mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"(Peu de joueurs : un seul étage.)","color":"dark_gray","italic":true}]
scoreboard players set $tff mg.st 0
