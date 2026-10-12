# Plus aucun innocent
function mg:mm/reveal
tellraw @a [{"text":"🔪 Le tueur a éliminé tout le monde !","color":"red","bold":true}]
execute as @a[tag=mg.play,tag=mg.mmm] run return run function mg:core/win_player
function mg:core/draw
