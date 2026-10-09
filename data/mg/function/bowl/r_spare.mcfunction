# SPARE (frame normal)
data modify storage mg:bowl w.b set value "/"
function mg:bowl/mw with storage mg:bowl w
scoreboard players set #pn mg.st 1
function mg:bowl/push
scoreboard players set @s mg.bfs 0
scoreboard players set @s mg.bxs 0
scoreboard players set #ev mg.st 2
function mg:bowl/next_frame
