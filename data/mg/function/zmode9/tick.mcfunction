execute if score $game mg.st matches 249 as @a[tag=mg.play,scores={mg.qs=1..}] if items entity @s weapon.mainhand *[custom_data~{zrpg:1b}] at @s run function mg:zx/rpg_fire
function mg:gun/tick
execute if score $game mg.st matches 249 run function mg:zm9/tick
execute if score $game mg.st matches 250 run function mg:inf9/tick
