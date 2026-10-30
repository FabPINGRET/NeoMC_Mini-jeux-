kill @e[tag=wv_platform_target,distance=0..]

summon marker -12401 123 343 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","1"]}
summon marker -12398 123 341 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","1"]}
summon marker -12396 123 338 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","1"]}

summon marker -12388 123 335 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","2"]}
summon marker -12384 123 335 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","2"]}
summon marker -12380 123 335 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","2"]}

summon marker -12372 123 338 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","3"]}
summon marker -12370 123 341 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","3"]}
summon marker -12367 123 343 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","3"]}

summon marker -12364 123 351 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","4"]}
summon marker -12364 123 355 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","4"]}
summon marker -12364 123 359 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","4"]}

summon marker -12367 123 367 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","5"]}
summon marker -12370 123 369 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","5"]}
summon marker -12372 123 372 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","5"]}

summon marker -12380 123 375 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","6"]}
summon marker -12384 123 375 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","6"]}
summon marker -12388 123 375 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","6"]}

summon marker -12396 123 372 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","7"]}
summon marker -12398 123 369 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","7"]}
summon marker -12401 123 367 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","7"]}

summon marker -12404 123 359 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","8"]}
summon marker -12404 123 355 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","8"]}
summon marker -12404 123 351 {NoGravity:1b,Silent:1b,Tags:["wv_platform_target","8"]}

execute as @n[tag=targeted,distance=0..] at @s run tag @n[tag=wv_platform_target,distance=0..] add nearest

kill @e[tag=wv_platform_target,tag=!nearest,distance=0..]
tag @e[tag=wv_platform_target,distance=0..] remove nearest
