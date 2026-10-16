execute if score $game mg.st matches 235 as @a[tag=mg.play,scores={mg.qs=1..}] if items entity @s weapon.mainhand *[custom_data~{zrpg:1b}] at @s run function mg:zx/rpg_fire
function mg:gun/tick
execute if score $game mg.st matches 235 run function mg:zm6/tick
execute if score $game mg.st matches 236 run function mg:inf6/tick
