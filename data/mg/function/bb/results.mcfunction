# Classement final
scoreboard players set $bbp mg.st 3
scoreboard players add @a[tag=mg.play,scores={mg.bi=0..}] mg.ba 0
scoreboard players set $bbmx mg.st 0
execute as @a[tag=mg.play,scores={mg.bi=0..}] run scoreboard players operation $bbmx mg.st > @s mg.ba
execute if score $bbmx mg.st matches 0 run return run function mg:bb/no_votes
tellraw @a[tag=mg.play] [{"text":"\n★ RÉSULTATS — thème : ","color":"gold","bold":true},{"nbt":"word","storage":"mg:bb","color":"yellow","bold":true}]
tag @a remove mg.brk
scoreboard players set $bbrk mg.st 1
function mg:bb/rank_next
execute as @a[tag=mg.play,scores={mg.bi=0..}] if score @s mg.ba = $bbmx mg.st run function mg:bb/win_one
execute as @a[tag=mg.win,limit=1] run scoreboard players operation $bbk mg.st = @s mg.bi
function mg:bb/vote_view
tag @a remove mg.brk
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 400
title @a[tag=mg.play] title [{"selector":"@a[tag=mg.win]","color":"gold","bold":true}]
title @a[tag=mg.play] subtitle [{"text":"signe la plus belle construction !","color":"yellow"}]
execute as @a at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
