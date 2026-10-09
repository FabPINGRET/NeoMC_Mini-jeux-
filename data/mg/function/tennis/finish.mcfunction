# Tous les courts sont finis : vainqueur(s) = gagnants humains de chaque court
execute unless score $state mg.st matches 2 run return 0
execute store result score $tnq mg.st if entity @a[tag=mg.tnwin,tag=mg.play]
execute if score $tnq mg.st matches 0 run return run function mg:core/draw
execute if score $tnq mg.st matches 1 as @a[tag=mg.tnwin,tag=mg.play,limit=1] run return run function mg:core/win_player
function mg:tennis/win_multi
