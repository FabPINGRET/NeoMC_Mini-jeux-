bossbar set boss:mind_contagion value 180
bossbar set boss:mind_contagion color green
bossbar set boss:mind_contagion players

tp @n[tag=mind_boss_stand,distance=0..] -11760 173 -196 0 0
function boss:mini/mind_contagion/mouth_end
kill @n[tag=mind_boss,distance=0..]
kill @e[tag=mind_clone,distance=0..]
kill @e[tag=m_monster_hard,distance=0..]


fill -11755 148 -178 -11739 147 -177 air replace minecraft:redstone_block
setblock -11757 147 -177 air

scoreboard players set mind_contagion bool 0

function boss:mini/mind_contagion/attacks/tentacle_finish
