bossbar set boss:mime value 180
bossbar set boss:mime color green
bossbar set boss:mime players

setblock -11661 149 -370 air

function boss:mini/mime_in_charge/arena_reset

setblock -11665 150 -337 air
tp @n[tag=mime_stand,distance=0..] -11648 164 -350 0 0
data modify entity @n[tag=mime_stand,distance=0..] Pose set value {}
setblock -11647 164 -350 minecraft:oak_sign[rotation=0,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:["","","",""]},components:{},front_text:{color:"black",has_glowing_text:0b,messages:["","Talk to the","Mime",""]},is_waxed:0b}
setblock -11647 164 -349 minecraft:stone_button[face=floor,facing=north,powered=false]
fill -11648 164 -339 -11648 165 -339 minecraft:air
setblock -11668 149 -337 air
setblock -11665 150 -339 air

item replace entity @n[tag=mime_stand,distance=0..] weapon.mainhand with air
item replace entity @n[tag=mime_stand,distance=0..] weapon.offhand with air
setblock -11663 150 -337 air
setblock -11665 149 -341 minecraft:black_wool
setblock -11666 149 -370 air
fill -11663 150 -369 -11664 150 -369 air
clone -11641 149 -345 -11639 149 -343 -11641 149 -341
