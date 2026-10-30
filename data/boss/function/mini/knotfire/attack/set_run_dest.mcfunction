kill @e[tag=knotfire_run_dest,distance=0..]

execute if entity @e[tag=knotfire_statue,tag=1,tag=active,distance=0..] run summon marker -10711 72 89 {NoGravity:1b,Silent:1b,Tags:["knotfire_run_dest"]}
execute if entity @e[tag=knotfire_statue,tag=1,tag=active,distance=0..] run summon marker -10683 72 89 {NoGravity:1b,Silent:1b,Tags:["knotfire_run_dest"]}

execute if entity @e[tag=knotfire_statue,tag=2,tag=active,distance=0..] run summon marker -10685 72 94 {NoGravity:1b,Silent:1b,Tags:["knotfire_run_dest"]}
execute if entity @e[tag=knotfire_statue,tag=2,tag=active,distance=0..] run summon marker -10709 72 84 {NoGravity:1b,Silent:1b,Tags:["knotfire_run_dest"]}

execute if entity @e[tag=knotfire_statue,tag=3,tag=active,distance=0..] run summon marker -10706 72 80 {NoGravity:1b,Silent:1b,Tags:["knotfire_run_dest"]}
execute if entity @e[tag=knotfire_statue,tag=3,tag=active,distance=0..] run summon marker -10688 72 98 {NoGravity:1b,Silent:1b,Tags:["knotfire_run_dest"]}

execute if entity @e[tag=knotfire_statue,tag=4,tag=active,distance=0..] run summon marker -10692 72 101 {NoGravity:1b,Silent:1b,Tags:["knotfire_run_dest"]}
execute if entity @e[tag=knotfire_statue,tag=4,tag=active,distance=0..] run summon marker -10702 72 77 {NoGravity:1b,Silent:1b,Tags:["knotfire_run_dest"]}

execute if entity @e[tag=knotfire_statue,tag=5,tag=active,distance=0..] run summon marker -10697 72 75 {NoGravity:1b,Silent:1b,Tags:["knotfire_run_dest"]}
execute if entity @e[tag=knotfire_statue,tag=5,tag=active,distance=0..] run summon marker -10697 72 103 {NoGravity:1b,Silent:1b,Tags:["knotfire_run_dest"]}

execute if entity @e[tag=knotfire_statue,tag=6,tag=active,distance=0..] run summon marker -10702 72 101 {NoGravity:1b,Silent:1b,Tags:["knotfire_run_dest"]}
execute if entity @e[tag=knotfire_statue,tag=6,tag=active,distance=0..] run summon marker -10692 72 77 {NoGravity:1b,Silent:1b,Tags:["knotfire_run_dest"]}

execute if entity @e[tag=knotfire_statue,tag=7,tag=active,distance=0..] run summon marker -10688 72 80 {NoGravity:1b,Silent:1b,Tags:["knotfire_run_dest"]}
execute if entity @e[tag=knotfire_statue,tag=7,tag=active,distance=0..] run summon marker -10706 72 98 {NoGravity:1b,Silent:1b,Tags:["knotfire_run_dest"]}

execute if entity @e[tag=knotfire_statue,tag=8,tag=active,distance=0..] run summon marker -10709 72 94 {NoGravity:1b,Silent:1b,Tags:["knotfire_run_dest"]}
execute if entity @e[tag=knotfire_statue,tag=8,tag=active,distance=0..] run summon marker -10685 72 84 {NoGravity:1b,Silent:1b,Tags:["knotfire_run_dest"]}

execute as @n[tag=knotfire_statue,tag=active,distance=0..] at @s run kill @n[tag=knotfire_run_dest,distance=0..]
