# Kart : préparation pendant le compte à rebours (zone chargée, pilotes sur la grille, karts dès que la zone est prête)
execute unless score $ktr mg.st matches 1..3 run scoreboard players set $ktr mg.st 1
execute unless score $kbat mg.st matches 0..1 run scoreboard players set $kbat mg.st 0
execute if score $ktr mg.st matches 3 unless data storage mg:kart built3 run tellraw @a [{"text":"⚠ L'arène de bataille est encore en construction : course sur le Circuit Champignon.","color":"gold"}]
execute if score $ktr mg.st matches 3 unless data storage mg:kart built3 run scoreboard players set $kbat mg.st 0
execute if score $ktr mg.st matches 3 unless data storage mg:kart built3 run scoreboard players set $ktr mg.st 1
tag @a remove mg.kout
tag @a remove mg.kok
scoreboard players set $kfl mg.st 0
scoreboard players set $kms mg.st -1
scoreboard players set $kmc mg.st 0
scoreboard players set @a[tag=mg.play] mg.krl 0
scoreboard players set #k2 mg.st 2
scoreboard players set $kwait mg.st 0
scoreboard players set #k10 mg.st 10
scoreboard players set $kouto mg.st 0
scoreboard players set @a[tag=mg.play] mg.kbl 0
scoreboard players enable @a[tag=mg.play] mg.kch
execute as @a[tag=mg.play] run function mg:kart/show_models
tellraw @a[tag=mg.play] [{"text":"\n🎥 ","color":"aqua"},{"text":"Avant le départ : appuie sur ","color":"white"},{"text":"F5","color":"yellow","bold":true},{"text":" pour conduire en vue 3e personne (derrière ton kart). Ton objet est dans toute la barre : clic droit pour l'utiliser.\n","color":"white"}]
execute if score $ktr mg.st matches 2 unless data storage mg:kart built2 run tellraw @a [{"text":"⚠ Le Royaume Koopa est encore en construction : course sur le Circuit Champignon.","color":"gold"}]
execute if score $ktr mg.st matches 2 unless data storage mg:kart built2 run scoreboard players set $ktr mg.st 1
function mg:kart/const
function mg:kart/fl_add
scoreboard players set #km1 mg.st -1
scoreboard players set #k3 mg.st 3
scoreboard players set #k4 mg.st 4
scoreboard players set #k5 mg.st 5
scoreboard players set #k8 mg.st 8
scoreboard players set #k20 mg.st 20
scoreboard players set #k100 mg.st 100
scoreboard players set #kt85 mg.st 85
scoreboard players set #kt120 mg.st 120
scoreboard players set #kt90 mg.st 90
scoreboard players set #k1000 mg.st 1000
scoreboard players set #k60 mg.st 60
scoreboard players set #k12 mg.st 12
scoreboard players set #k65 mg.st 65
scoreboard players set #k120 mg.st 120
scoreboard players set #kkmh mg.st 108
scoreboard players set $ktime mg.st 0
scoreboard players set $kfo mg.st 0
scoreboard players set $kend mg.st 0
scoreboard players set $kph mg.st 0
scoreboard players set $gi mg.st 0
kill @e[tag=mg.ib]
kill @e[tag=mg.kpart]
kill @e[tag=mg.kcam]
kill @e[tag=mg.khz]
gamemode adventure @a[tag=mg.play]
clear @a[tag=mg.play]
tag @a remove mg.kfin
scoreboard players set @a[tag=mg.play] mg.ksp 0
scoreboard players set @a[tag=mg.play] mg.kdr 0
scoreboard players set @a[tag=mg.play] mg.krc 0
scoreboard players set @a[tag=mg.play] mg.kbo 0
scoreboard players set @a[tag=mg.play] mg.khi 0
scoreboard players set @a[tag=mg.play] mg.kst 0
scoreboard players set @a[tag=mg.play] mg.kit 0
scoreboard players set @a[tag=mg.play] mg.kic 0
scoreboard players set @a[tag=mg.play] mg.kgd 0
scoreboard players set @a[tag=mg.play] mg.kbill 0
scoreboard players set @a[tag=mg.play] mg.kboo 0
scoreboard players set @a[tag=mg.play] mg.kmg 0
scoreboard players set @a[tag=mg.play] mg.kcp 0
scoreboard players set @a[tag=mg.play] mg.klp 0
scoreboard players set @a[tag=mg.play] mg.kvy 0
scoreboard players set @a[tag=mg.play] mg.kfp 0
scoreboard players set @a[tag=mg.play] mg.kps 0
scoreboard players set @a[tag=mg.play] mg.kvm 1
scoreboard players set @a[tag=mg.play] mg.kof 0
scoreboard players reset @a mg.qs
execute as @a[tag=mg.play] run function mg:kart/place_one
function mg:kart/standings_init
schedule function mg:kart/place_all 40t
