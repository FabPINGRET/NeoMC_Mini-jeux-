# 📞 Téléphone — préparation (id 81) : 5 à 12 joueurs, une chaîne par joueur
tag @a remove mg.tdone
scoreboard players reset @a mg.ti
scoreboard players reset @a mg.tc
scoreboard players set @a[tag=mg.play] mg.tpt 0
scoreboard players set $tp mg.st -1
scoreboard players set $tt mg.st 0
execute store result score $tn mg.st if entity @a[tag=mg.play]
execute if score $tn mg.st matches ..4 run return run function mg:tel/too_few
execute if score $tn mg.st matches 13.. run scoreboard players set $tn mg.st 12
scoreboard players set $tk mg.st 0
execute as @a[tag=mg.play,sort=random] run function mg:tel/assign
function mg:bb/words_init
data modify storage mg:tel ch set value []
scoreboard players set $tk mg.st 0
function mg:tel/init_ch
function mg:tel/fl_add
function mg:tel/room
schedule function mg:tel/plots 40t
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
tp @a[tag=mg.play] 0.5 64 19420.5
execute as @a[tag=mg.play] run spawnpoint @s 0 64 19420
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 66
scoreboard players set $pz mg.st 19420
tellraw @a[tag=mg.play] [{"text":"📞 TÉLÉPHONE : ","color":"gold","bold":true},{"text":"écris un mot → un autre le construit → un autre devine → un autre construit → un dernier devine. À la fin, on découvre ce que chaque mot est devenu !","color":"gray"}]
execute if entity @a[tag=mg.play,scores={mg.ti=-1}] run tellraw @a[tag=mg.play,scores={mg.ti=-1}] {"text":"(12 joueurs maximum : tu regardes cette partie.)","color":"dark_gray","italic":true}
