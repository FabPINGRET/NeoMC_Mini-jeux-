# TNT Run — préparation
execute if score $ar mg.st matches 1.. run return run function mg:var/mode/tntrun_prepare
function mg:tntrun/build

scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 92
scoreboard players set $pz mg.st 600
scoreboard players set $dk mg.st 9

gamemode adventure @a[tag=mg.play]
execute as @a[tag=mg.play] run spawnpoint @s 0 92 600
spreadplayers 0 600 4 13 under 86 false @a[tag=mg.play]
