function game:firelight/exit/narrator

function game:firelight/set/empty
function game:firelight/scene/empty

function game:firelight/set_change

scoreboard players set firelight_script Value -1

execute positioned 9882 61 -126 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute positioned 9882 61 -126 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"\n<"},{"text":"Dark Bob Saget","color":"#D47453"},{"text":"> What a nice play to be sure! In my opinion, it was derailed from perfection","color":"white"},{"text":" just before the halfway point","color":"green"},{"text":". We can take it from the top whenever you're ready!","color":"white"}]
