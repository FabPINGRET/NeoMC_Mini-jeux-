scoreboard players set boss:wm BossHealth 6
bossbar set boss:wm players
bossbar set boss:wm value 6
bossbar set boss:wm color green

tag @a[tag=mg.flw] remove bossroom

# Reset Start Latch
setblock -11249 -35 -132 air

# Turn off Boss Tick
setblock -11245 -34 -132 air

# Turn off slam check
setblock -11199 -35 -105 air

# Turn off Pick Attack
setblock -11219 -35 -131 air
schedule clear floaty:sched/boss/9/pick_attack

# DRAW is anchor for drawing boss and faces target, POS is current position of body and faces DEST, DEST is the location POS is trying to move to
kill @e[tag=wm_drone_pos,distance=0..]
kill @e[tag=wm_drone_dest,distance=0..]
kill @e[tag=wm_drone_pivot,distance=0..]
kill @e[tag=wm_drone_part,distance=0..]
kill @e[tag=wm_drone_draw,distance=0..]
kill @e[tag=encruster,distance=0..]

function boss:9/arena/quick_dry
function boss:9/arena/barnacle_place

#INIT VIEW MODES
scoreboard players set @e[tag=wm_drone_draw,distance=0..] Value 0

scoreboard players set @e[tag=wm_drone_pos,distance=0..] Value 0
scoreboard players set @e[tag=wm_drone_pivot,distance=0..] Value 1
scoreboard players set @e[tag=wm_drone_pivot,distance=0..] bool 0
scoreboard players set wm_follow_dest bool 1
