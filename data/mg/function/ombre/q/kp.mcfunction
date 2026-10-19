# @s : un monstre de plus pour l'étape (objectif $(n))
scoreboard players add @s mg.olqp 1
$execute if score @s mg.olqp matches $(n).. run return run function mg:ombre/q/adv
$tellraw @s [{"text":"⚔ Progression : ","color":"gold"},{"score":{"name":"@s","objective":"mg.olqp"},"color":"yellow","bold":true},{"text":" / $(n)","color":"yellow"}]
