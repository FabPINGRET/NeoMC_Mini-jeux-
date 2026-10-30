fill ~3 116 ~1 ~-3 116 ~-1 minecraft:sweet_berry_bush[age=1] replace short_grass strict
fill ~1 116 ~3 ~-1 116 ~-3 minecraft:sweet_berry_bush[age=1] replace short_grass strict
fill ~2 116 ~2 ~-2 116 ~-2 minecraft:sweet_berry_bush[age=1] replace short_grass strict

particle minecraft:totem_of_undying ~ 116.5 ~ 2 0.5 2 0.2 30

playsound minecraft:entity.player.hurt_sweet_berry_bush block @a[tag=mg.flw] ~ 116 ~ 3 1
setblock -10060 116 322 air
