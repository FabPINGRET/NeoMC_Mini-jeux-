# Le tueur est mort, ou il reste des innocents à la fin
function mg:mm/reveal
tag @a[tag=mg.play,tag=!mg.mmm] add mg.win
scoreboard players add @a[tag=mg.play,tag=!mg.mmm] mg.wins 1
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 120
title @a[tag=!mg.surv] title {"text":"Les INNOCENTS gagnent !","color":"green","bold":true}
tellraw @a [{"text":"★ Victoire des innocents : ","color":"gold"},{"selector":"@a[tag=mg.play,tag=!mg.mmm]","color":"green"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
