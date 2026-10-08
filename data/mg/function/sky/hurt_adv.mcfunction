# Touché par une flèche ou une charge de vent d'un joueur (@s = victime) — avancement mg:sky/hurt
advancement revoke @s only mg:sky/hurt
execute unless score $game mg.st matches 75 run return 0
execute unless score $state mg.st matches 2 run return 0
execute unless score $elm mg.st matches 2 run return 0
execute unless entity @s[tag=mg.play] run return 0
tag @a remove mg.skak
execute on attacker run tag @s[tag=mg.play] add mg.skak
execute if entity @s[tag=mg.skak] run return run tag @a remove mg.skak
function mg:sky/stun
tag @a remove mg.skak
