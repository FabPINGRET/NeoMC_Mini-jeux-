execute if score $game mg.st matches 212 as @a[tag=mg.play,scores={mg.qs=1..}] if items entity @s weapon.mainhand *[custom_data~{zrpg:1b}] at @s run function mg:zx/rpg_fire
function mg:gun/tick
execute if score $game mg.st matches 212 run function mg:zm3/tick
execute if score $game mg.st matches 213 run function mg:inf3/tick
