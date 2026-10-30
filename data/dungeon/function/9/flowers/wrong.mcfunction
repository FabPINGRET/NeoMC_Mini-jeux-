setblock -11023 81 -203 light[level=15]
setblock -11021 81 -204 light[level=15]
setblock -11019 81 -204 light[level=15]
setblock -11017 81 -204 light[level=15]
setblock -11015 81 -203 light[level=15]

# Disable guessing
setblock -11026 59 -203 minecraft:redstone_block

playsound minecraft:zelda.error master @a[tag=mg.flw] -11019 82 -207 1 1

#restore center button
setblock -11028 59 -201 minecraft:redstone_block

function dungeon:9/flowers/reset_tapes
