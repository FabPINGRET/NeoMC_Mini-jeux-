# Révélation : chaîne par chaîne (mot → construction → devinette → construction → devinette)
clear @a[tag=mg.play]
gamemode spectator @a[tag=mg.play]
scoreboard objectives setdisplay sidebar mg.tpt
scoreboard players set $rc mg.st 0
scoreboard players set $rs mg.st -1
scoreboard players set $tt mg.st 0
scoreboard players set $tlim mg.st 1
tellraw @a[tag=!mg.surv] {"text":"\n📞 RÉVÉLATION ! Voici ce que chaque mot est devenu…","color":"gold","bold":true}
