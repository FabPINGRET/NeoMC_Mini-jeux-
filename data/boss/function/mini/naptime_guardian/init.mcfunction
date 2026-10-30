setblock -11554 189 -349 air

bossbar set boss:teddybear value 180
bossbar set boss:teddybear color green
bossbar set boss:teddybear players

setblock -11545 205 -336 minecraft:oak_sign[rotation=0,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:["","","",""]},components:{},front_text:{color:"black",has_glowing_text:0b,messages:["","Talk to the","Teddybear",""]},is_waxed:0b}
setblock -11545 205 -335 minecraft:polished_blackstone_button[face=floor,facing=north,powered=false]
tp @n[tag=naptime_stand,distance=0..] -11545.5 204.67 -335.5 0 0
function boss:mini/naptime_guardian/pose/idle

setblock -11560 189 -326 air
fill -11546 205 -325 -11546 206 -325 air

fill -11535 204 -325 -11557 204 -347 minecraft:green_wool replace minecraft:yellow_wool

fill -11535 205 -325 -11557 206 -347 minecraft:air replace oak_fence
kill @n[tag=nap_boss,tag=enemy,distance=0..]
fill -11553 190 -345 -11553 190 -347 air
setblock -11543 189 -349 minecraft:air
setblock -11546 205 -336 air
