# Étape 17 validée (sigrun)
execute unless score @s mg.olm1 matches 5.. run return run tellraw @s [{"text":"Il te faut 5 × peau de bête (tu en as ","color":"red"},{"score":{"name":"@s","objective":"mg.olm1"},"color":"yellow"},{"text":").","color":"red"}]
scoreboard players remove @s mg.olm1 5
function mg:ombre/xp {n:150}
scoreboard players set @s mg.olfur 1
tellraw @s {"text":"🧥 Cape de fourrure : tu ne crains plus le froid de Givrecroc.","color":"aqua"}
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
