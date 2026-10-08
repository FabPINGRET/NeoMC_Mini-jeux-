# Mise à jour du tableau de droite (toutes les 10 ticks, état 2)
scoreboard players add $sbt mg.st 1
execute if score $sbt mg.st matches ..9 run return 0
scoreboard players set $sbt mg.st 0
scoreboard players reset * mg.sbg
execute store result storage mg:c sb.n int 1 if entity @a[tag=mg.play]
# Jeux « dernier debout » : les survivants, triés par leur score du jeu
execute if score $game mg.st matches 22 as @a[tag=mg.play] run scoreboard players operation @s mg.sbg = @s mg.lv
execute if score $game mg.st matches 23 as @a[tag=mg.play] run scoreboard players operation @s mg.sbg = @s mg.dp
execute unless score $game mg.st matches 4..7 unless score $game mg.st matches 22..23 as @a[tag=mg.play] run scoreboard players set @s mg.sbg 0
execute if score $game mg.st matches 22..23 run scoreboard players display numberformat @a[tag=mg.play] mg.sbg styled {"color":"gold"}
execute if score $game mg.st matches 27 run scoreboard players display numberformat @a[tag=mg.play,tag=mg.bomb] mg.sbg fixed {"text":"✹ BOMBE","color":"red","bold":true}
execute unless score $game mg.st matches 4..7 run scoreboard players set #sbh mg.sbg 1000
execute unless score $game mg.st matches 4..7 run function mg:sb/hdr with storage mg:c sb
# Jeux d'équipes : joueurs restants par équipe (Bedwars : état du lit)
execute if score $game mg.st matches 4..7 run function mg:sb/teams
