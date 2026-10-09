# STRIKE (frame normal)
data modify storage mg:bowl w.a set value ""
data modify storage mg:bowl w.b set value "X"
data modify storage mg:bowl w.c set value ""
function mg:bowl/mw with storage mg:bowl w
scoreboard players set #pn mg.st 2
function mg:bowl/push
scoreboard players set @s mg.bfs 0
scoreboard players add @s mg.bxs 1
scoreboard players set #ev mg.st 1
function mg:bowl/next_frame
