# @s passe son niveau (mg.dlv) : niveau suivant, sans point de réussite (mg.dok inchangé)
scoreboard players set @s mg.dkc 0
scoreboard players add @s mg.dsk 1
tellraw @a[tag=mg.play] [{"text":"⏭ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" passe le niveau ","color":"gray"},{"score":{"name":"@s","objective":"mg.dlv"},"color":"aqua","bold":true},{"text":" (non réussi)","color":"gray"}]
execute at @s run playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 0.8 1.2
scoreboard players add @s mg.dlv 1
execute if score @s mg.dlv matches 14.. if score $game mg.st matches 228 run return run function mg:dropadv/s_done
execute if score @s mg.dlv matches 14.. run return run function mg:dropadv/finish
execute if score $game mg.st matches 228 run scoreboard players add @s mg.dtt 1
execute if score $game mg.st matches 228 run scoreboard players set @s mg.dtr 1
function mg:dropadv/spawn
function mg:dropadv/show_level
