#remove active
fill -11796 232 310 -11796 242 350 air replace gold_block
fill -11810 232 364 -11850 242 364 air replace gold_block
fill -11864 232 350 -11864 242 310 air replace gold_block
fill -11850 232 296 -11810 242 296 air replace gold_block

#fix walls
fill -11795 236 311 -11795 232 349 minecraft:black_concrete replace air
fill -11795 234 311 -11795 232 349 minecraft:coal_block replace minecraft:black_concrete
fill -11795 234 311 -11795 232 349 minecraft:coal_block replace minecraft:ochre_froglight
fill -11811 232 365 -11850 236 365 minecraft:black_concrete replace air
fill -11811 232 365 -11850 234 365 minecraft:coal_block replace minecraft:black_concrete
fill -11811 232 365 -11850 234 365 minecraft:coal_block replace minecraft:ochre_froglight
fill -11865 232 350 -11865 236 310 minecraft:black_concrete replace air
fill -11865 232 350 -11865 234 310 minecraft:coal_block replace minecraft:black_concrete
fill -11865 232 350 -11865 234 310 minecraft:coal_block replace minecraft:ochre_froglight
fill -11850 232 295 -11810 236 295 minecraft:black_concrete replace air
fill -11850 232 295 -11810 234 295 minecraft:coal_block replace minecraft:black_concrete
fill -11850 232 295 -11810 234 295 minecraft:coal_block replace minecraft:ochre_froglight

#replace faces
clone -11859 202 342 -11859 210 348 -11796 234 310
clone -11859 202 342 -11859 210 348 -11796 234 327
clone -11859 202 342 -11859 210 348 -11796 234 344
clone -11859 202 342 -11859 210 348 -11864 234 344
clone -11859 202 342 -11859 210 348 -11864 234 327
clone -11859 202 342 -11859 210 348 -11864 234 310

clone -11859 202 348 -11853 210 348 -11850 234 364
clone -11859 202 348 -11853 210 348 -11833 234 364
clone -11859 202 348 -11853 210 348 -11816 234 364
clone -11859 202 348 -11853 210 348 -11816 234 296
clone -11859 202 348 -11853 210 348 -11833 234 296
clone -11859 202 348 -11853 210 348 -11850 234 296

setblock -11801 203 351 air
