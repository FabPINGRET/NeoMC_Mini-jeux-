# @s a gagné au moins un niveau général
tellraw @s [{"text":"🏅 Niveau général ","color":"aqua","bold":true},{"score":{"name":"@s","objective":"mg.lvl"},"color":"yellow","bold":true},{"text":" !","color":"aqua","bold":true},{"text":"  (score ","color":"gray","bold":false},{"score":{"name":"@s","objective":"mg.gen"},"color":"gray"},{"text":")","color":"gray"}]
execute at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.8 1.2
execute if score @s mg.lvl matches 5.. run tellraw @a[tag=!mg.surv] [{"text":"🏅 ","color":"aqua"},{"selector":"@s","color":"yellow"},{"text":" passe niveau général ","color":"gray"},{"score":{"name":"@s","objective":"mg.lvl"},"color":"aqua","bold":true}]
function mg:hall/top {obj:"mg.lvl",key:"gen",lbl:"🏅 Meilleur niveau général",col:"aqua",unit:" niv."}
