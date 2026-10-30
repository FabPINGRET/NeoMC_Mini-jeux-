tp @n[tag=mind_boss,distance=0..] -11760 173 -196

execute positioned -11760 173 -196 run function summon:mind_clone
execute positioned -11760 173 -196 run function summon:mind_clone
execute positioned -11760 173 -196 run function summon:mind_clone

function boss:mini/mind_contagion/attacks/tentacle_start

playsound minecraft:entity.warden.roar hostile @a[tag=mg.flw] -11760 173 -196 2 2
