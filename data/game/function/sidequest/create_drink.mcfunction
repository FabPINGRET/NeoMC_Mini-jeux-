execute if blocks 127 46 -55 137 48 -55 127 46 -57 masked run setblock 128 42 -47 minecraft:redstone_block
execute if blocks 127 46 -55 137 48 -55 127 46 -60 masked run setblock 128 42 -46 minecraft:redstone_block
execute if blocks 127 46 -55 137 48 -55 127 46 -63 masked run setblock 128 42 -45 minecraft:redstone_block

execute if block 127 46 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[0.00,0.60,0.00]} 137 47.5 -50 0.1 0.1 0.1 0 2 force
execute if block 128 46 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[1.00,1.00,0.60]} 137 47.5 -50 0.1 0.1 0.1 0 2 force
execute if block 129 46 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[0.90,0.90,0.00]} 137 47.5 -50 0.1 0.1 0.1 0 2 force

execute if block 131 46 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[0.20,0.15,0.15]} 137 47.5 -50 0.1 0.1 0.1 0 2 force
execute if block 132 46 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[0.90,0.40,0.05]} 137 47.5 -50 0.1 0.1 0.1 0 2 force
execute if block 133 46 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[0.95,0.80,0.20]} 137 47.5 -50 0.1 0.1 0.1 0 2 force

execute if block 135 46 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[0.70,1.00,0.60]} 137 47.5 -50 0.1 0.1 0.1 0 2 force
execute if block 136 46 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[0.80,0.20,1.00]} 137 47.5 -50 0.1 0.1 0.1 0 2 force
execute if block 137 46 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[0.70,0.20,0.00]} 137 47.5 -50 0.1 0.1 0.1 0 2 force

execute if block 127 48 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[0.10,0.80,1.00]} 137 47.5 -50 0.1 0.1 0.1 0 2 force
execute if block 128 48 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[1.00,0.80,0.10]} 137 47.5 -50 0.1 0.1 0.1 0 2 force
execute if block 129 48 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[1.00,0.50,0.80]} 137 47.5 -50 0.1 0.1 0.1 0 2 force

execute if block 131 48 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[1.00,0.00,0.00]} 137 47.5 -50 0.1 0.1 0.1 0 2 force
execute if block 132 48 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[0.90,0.50,1.00]} 137 47.5 -50 0.1 0.1 0.1 0 2 force
execute if block 133 48 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[0.00,0.40,0.00]} 137 47.5 -50 0.1 0.1 0.1 0 2 force

execute if block 135 48 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[0.75,0.55,0.40]} 137 47.5 -50 0.1 0.1 0.1 0 2 force
execute if block 136 48 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[1.00,0.90,0.70]} 137 47.5 -50 0.1 0.1 0.1 0 2 force
execute if block 137 48 -55 redstone_lamp[lit=true] run particle dust{scale:1,color:[0.10,0.80,1.00]} 137 47.5 -50 0.1 0.1 0.1 0 2 force

playsound minecraft:item.bottle.fill master @a[tag=mg.flw] 137 47 -50 1 2
