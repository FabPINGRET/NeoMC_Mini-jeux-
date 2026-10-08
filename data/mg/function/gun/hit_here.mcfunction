# Cible touchée à cet endroit (le sniper traverse, le Ray Gun explose)
execute as @e[tag=mg.ghit,limit=1] run function mg:gun/hit
tag @e[tag=mg.ghit] remove mg.ghit
execute if score $gdn mg.st matches 6 run function mg:gun/splash
execute unless score $gdn mg.st matches 5 run scoreboard players set $gstop mg.st 1
