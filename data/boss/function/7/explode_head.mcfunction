fill -10469 -21 -382 -10477 -15 -374 air
setblock -10473 -21 -378 minecraft:chiseled_deepslate
setblock -10471 -21 -380 minecraft:polished_deepslate
setblock -10471 -21 -376 minecraft:polished_deepslate
setblock -10475 -21 -376 minecraft:polished_deepslate
setblock -10475 -21 -380 minecraft:polished_deepslate
particle minecraft:explosion -10473 -18 -378 2 2 2 0 20
particle minecraft:block_crumble{block_state:"polished_deepslate"} -10473 -18 -378 2 2 2 0 200
particle minecraft:dust_pillar{block_state:"polished_deepslate"} -10473 -18 -378 2 2 2 0 200
particle smoke -10473 -18 -378 2 2 2 0.2 200
playsound minecraft:entity.dragon_fireball.explode master @a[tag=mg.flw] -10473 -21 -378 3 0.7 1
playsound minecraft:entity.iron_golem.damage master @a[tag=mg.flw] -10473 -21 -378 3 0.2 1
playsound minecraft:block.decorated_pot.shatter master @a[tag=mg.flw] -10473 -21 -378 3 0.2 1

setblock -10449 -48 -398 redstone_block
