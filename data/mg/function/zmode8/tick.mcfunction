execute if score $game mg.st matches 247 as @a[tag=mg.play,scores={mg.qs=1..}] if items entity @s weapon.mainhand *[custom_data~{zrpg:1b}] at @s run function mg:zx/rpg_fire
function mg:gun/tick
execute if score $game mg.st matches 247 run function mg:zm8/tick
execute if score $game mg.st matches 248 run function mg:inf8/tick
