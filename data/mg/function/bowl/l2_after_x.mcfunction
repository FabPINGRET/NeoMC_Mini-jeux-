# 2e lancer après un strike au dernier frame (lancer bonus)
function mg:bowl/mk_b
function mg:bowl/mw with storage mg:bowl w
scoreboard players set @s mg.brl 3
execute if score #k mg.st matches 10 run tag @s add mg.bnr
execute if score #k mg.st matches 10 run scoreboard players add @s mg.bxs 1
execute if score #k mg.st matches 10 run scoreboard players set #ev mg.st 1
execute unless score #k mg.st matches 10 run scoreboard players set @s mg.bxs 0
