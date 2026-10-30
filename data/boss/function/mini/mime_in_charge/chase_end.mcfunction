setblock -11658 149 -337 air

setblock -11665 150 -339 air

data modify entity @n[tag=mime_stand,distance=0..] Pose set value {}
item replace entity @n[tag=mime_stand,distance=0..] weapon.mainhand with air
item replace entity @n[tag=mime_stand,distance=0..] weapon.offhand with air

schedule function floaty:sched/boss/mini/mime_in_charge/ceiling/lower 1s
