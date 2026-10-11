# @s : présentoir cliqué
scoreboard players operation $lgn mg.st = @s mg.st
execute on target if entity @s[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw] run function mg:lobby/guns_give
execute if data entity @s attack on attacker if entity @s[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw] run function mg:lobby/guns_give
data remove entity @s interaction
data remove entity @s attack
