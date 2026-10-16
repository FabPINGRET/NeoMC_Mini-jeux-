# Banquise : préparation (zone chargée par ctf3/prepare)
execute unless score $state mg.st matches 1 run return 0
execute unless loaded -44 80 41476 run return run schedule function mg:ctf3/prepare_b 20t
execute unless loaded 44 80 41524 run return run schedule function mg:ctf3/prepare_b 20t
execute unless loaded 0 80 41500 run return run schedule function mg:ctf3/prepare_b 20t
# 🚩 Capture the Flag — préparation
function mg:ctf3/build
function mg:ctf3/kill_all
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 95
scoreboard players set $pz mg.st 41500
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
scoreboard players set $nt mg.st 2
function mg:core/assign_teams
scoreboard players reset Rouge mg.cf
scoreboard players reset Bleu mg.cf
function mg:ctf3/home_red
function mg:ctf3/home_blue
execute as @a[tag=mg.play] run function mg:ctf3/spawn
