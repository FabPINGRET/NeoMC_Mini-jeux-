# @s : plus joueur d'Ombrelune
function mg:ombre/cs/stop
title @s clear
title @s reset
team leave @s
function mg:ombre/stats_rm
xp set @s 0 levels
xp set @s 0 points
function mg:ombre/horse_gone
tag @s remove mg.olintro
