# Build Battle — préparation (jeux 57 = mot aléatoire, 58 = Maître du mot)
scoreboard players set $bbc10 mg.st 10
scoreboard players set $bbc20 mg.st 20
scoreboard players set $bbc60 mg.st 60
scoreboard players set $bbc100 mg.st 100
scoreboard players set $bbp mg.st -1
scoreboard players set $bbt mg.st 0
scoreboard players set $bbk mg.st -1
scoreboard players set $bbm mg.st 0
execute if score $game mg.st matches 58 run scoreboard players set $bbm mg.st 1
execute if score $bbm mg.st matches 1 if score $n0 mg.st matches ..2 run tellraw @a[tag=mg.play] [{"text":"✎ Il faut au moins 3 joueurs pour un Maître du mot : le thème sera tiré au hasard.","color":"gold"}]
execute if score $bbm mg.st matches 1 if score $n0 mg.st matches ..2 run scoreboard players set $bbm mg.st 0
scoreboard players set $bbs mg.st 0
execute if score $n0 mg.st matches 1 run scoreboard players set $bbs mg.st 1

# Remise à zéro des joueurs
tag @a remove mg.bm
tag @a remove mg.bme
tag @a remove mg.brk
tag @a remove mg.bfar
scoreboard players reset @a mg.bi
scoreboard players reset @a mg.br
scoreboard players reset @a mg.ba
scoreboard players reset @a mg.bb
scoreboard players reset @a mg.bw
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]

# Mots
function mg:bb/words_init
data remove storage mg:bb word

# Maître du mot (un joueur désigné avec /tag <joueur> add mg.bmx, sinon tirage au sort)
execute if score $bbm mg.st matches 1 if entity @a[tag=mg.play,tag=mg.bmx] run tag @r[tag=mg.play,tag=mg.bmx] add mg.bm
execute if score $bbm mg.st matches 1 unless entity @a[tag=mg.bm] run tag @r[tag=mg.play] add mg.bm
tag @a remove mg.bmx

# Parcelles : une par constructeur (12 max), les autres sont juges
scoreboard players set $bbn mg.st 0
execute as @a[tag=mg.play,tag=!mg.bm,sort=random] run function mg:bb/assign_one
scoreboard players set @a[tag=mg.play,tag=mg.bm] mg.bi -1
function mg:bb/build_used

# Perchoir des spectateurs = studio
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 70
scoreboard players set $pz mg.st 13650

# Téléportation
execute as @a[tag=mg.play,scores={mg.bi=0..}] run function mg:bb/tp_builder
tp @a[tag=mg.play,scores={mg.bi=-1}] 0.5 65 13650.5 0 10
execute if score $bbn mg.st matches 12.. if score $n0 mg.st matches 13.. run tellraw @a[tag=mg.play] [{"text":"✎ Plus de 12 joueurs : les derniers sont juges (ils votent sans construire).","color":"gray"}]
