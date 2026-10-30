clone 9925 58 -52 9925 58 -52 9925 58 -51 replace move
clone 9925 58 -53 9925 58 -53 9925 58 -52 replace move
clone 9925 58 -54 9925 58 -54 9925 58 -53 replace move
clone 9925 58 -55 9925 58 -55 9925 58 -54 replace move
clone 9925 58 -56 9925 58 -56 9925 58 -55 replace move
clone 9925 58 -57 9925 58 -57 9925 58 -56 replace move
clone 9925 58 -58 9925 58 -58 9925 58 -57 replace move
clone 9925 58 -59 9925 58 -59 9925 58 -58 replace move
clone 9925 58 -60 9925 58 -60 9925 58 -59 replace move
clone 9925 58 -61 9925 58 -61 9925 58 -60 replace move
clone 9925 58 -62 9925 58 -62 9925 58 -61 replace move
clone 9925 58 -63 9925 58 -63 9925 58 -62 replace move
clone 9925 58 -64 9925 58 -64 9925 58 -63 replace move
clone 9925 58 -65 9925 58 -65 9925 58 -64 replace move
clone 9925 58 -66 9925 58 -66 9925 58 -65 replace move
clone 9925 58 -67 9925 58 -67 9925 58 -66 replace move
clone 9925 58 -68 9925 58 -68 9925 58 -67 replace move
clone 9925 58 -69 9925 58 -69 9925 58 -68 replace move
clone 9926 58 -69 9926 58 -69 9925 58 -69 replace move
clone 9927 59 -69 9927 59 -69 9926 58 -69 replace move
clone 9928 59 -69 9928 59 -69 9927 59 -69 replace move
clone 9929 59 -69 9929 59 -69 9928 59 -69 replace move
clone 9930 59 -69 9930 59 -69 9929 59 -69 replace move
clone 9931 59 -69 9931 59 -69 9930 59 -69 replace move
clone 9932 59 -69 9932 59 -69 9931 59 -69 replace move

fill 9925 58 -65 9925 58 -65 bricks replace minecraft:magma_block

execute unless block 9925 58 -65 air run particle minecraft:cloud 9925 58 -65 0.5 0.5 0.5 0.05 50
execute unless block 9925 58 -65 air run playsound minecraft:block.fire.extinguish block @a[tag=mg.flw] 9925 58 -65 1 1
execute unless block 9926 58 -69 air run playsound minecraft:item.bottle.fill_dragonbreath block @a[tag=mg.flw] 9932 66 -69 1 1.5
execute unless block 9926 58 -69 air run summon falling_block 9932 66 -69 {BlockState:{Name:"minecraft:magma_block"},Time:1,FallHurtAmount:0f,Tags:["brickworks_falling"]}
execute unless block 9925 58 -51 air run summon falling_block 9925 58 -51 {BlockState:{Name:"minecraft:bricks"},Time:1,FallHurtAmount:0f,Tags:["brickworks_falling"]}
setblock 9925 58 -51 air
