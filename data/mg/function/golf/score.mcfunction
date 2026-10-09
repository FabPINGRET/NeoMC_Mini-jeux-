# @s : trou fini (mg.gfc coups) → total, tableau (−total, affiché comme « total (écart au par) »)
scoreboard players set @s mg.gfs 2
scoreboard players operation @s mg.gft += @s mg.gfc
scoreboard players operation @s mg.gfd = @s mg.gft
scoreboard players operation @s mg.gfd *= #gfm1 mg.st
function mg:golf/sb_fmt
