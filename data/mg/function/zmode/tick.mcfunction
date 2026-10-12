execute if score $game mg.st matches 97 as @a[tag=mg.play,scores={mg.qs=1..}] if items entity @s weapon.mainhand *[custom_data~{zrpg:1b}] at @s run function mg:zx/rpg_fire
function mg:gun/tick
execute if score $game mg.st matches 97 run function mg:zm/tick
execute if score $game mg.st matches 98 run function mg:inf/tick
