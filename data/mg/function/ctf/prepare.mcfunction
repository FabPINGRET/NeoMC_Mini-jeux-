# 🚩 Capture the Flag — préparation
function mg:ctf/build
function mg:ctf/kill_all
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 95
scoreboard players set $pz mg.st 21600
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
scoreboard players set $nt mg.st 2
function mg:core/assign_teams
scoreboard players reset Rouge mg.cf
scoreboard players reset Bleu mg.cf
function mg:ctf/home_red
function mg:ctf/home_blue
execute as @a[tag=mg.play] run function mg:ctf/spawn
