# @s atteint l'arrivée
scoreboard players operation $s mg.st = $sjt mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $s mg.st /= #20 mg.st
tellraw @a [{"text":"🏁 ","color":"aqua"},{"selector":"@s","color":"yellow","bold":true},{"text":" arrive en premier en ","color":"aqua"},{"score":{"name":"$s","objective":"mg.st"},"color":"yellow"},{"text":" s !","color":"aqua"}]
execute at @s run summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:20,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{explosions:[{shape:"star",colors:[I;65280,16776960]}]}}}}
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw
function mg:core/win_player
