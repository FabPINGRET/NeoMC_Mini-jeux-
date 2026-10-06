# Un joueur vient de frapper une entité (@s = attaquant) — avancement mg:tnt_hit
advancement revoke @s only mg:tnt_hit
execute unless score $game mg.st matches 27 run return 0
execute unless score $state mg.st matches 2 run return 0
execute unless entity @s[tag=mg.bomb,tag=mg.play] run return 0
# Victime : joueur proche sans la bombe, pas protégé
execute unless entity @a[tag=mg.play,tag=!mg.bomb,scores={mg.cd=0},distance=..6] run return 0
tag @a[tag=mg.play,tag=!mg.bomb,scores={mg.cd=0},distance=..6,limit=1,sort=nearest] add mg.newb
function mg:tnttag/pass
