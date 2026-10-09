# Plus de survivants
tellraw @a {"text":"🧟 Tout le monde est infecté !","color":"dark_green","bold":true}
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw
function mg:core/win_green
