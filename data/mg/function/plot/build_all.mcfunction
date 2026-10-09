# Construction des 15 plots (chunks forceloadés par plot/build) puis libération des chunks
function mg:plot/build_one {n:1,lx:89.5,lz:37.5,wx1:77,wx2:101,wz1:25,wz2:49,bx1:78,bx2:100,bz1:26,bz2:48,gx1:79,gx2:99,gz1:27,gz2:47}
function mg:plot/build_one {n:2,lx:68.5,lz:68.5,wx1:56,wx2:80,wz1:56,wz2:80,bx1:57,bx2:79,bz1:57,bz2:79,gx1:58,gx2:78,gz1:58,gz2:78}
function mg:plot/build_one {n:3,lx:37.5,lz:89.5,wx1:25,wx2:49,wz1:77,wz2:101,bx1:26,bx2:48,bz1:78,bz2:100,gx1:27,gx2:47,gz1:79,gz2:99}
function mg:plot/build_one {n:4,lx:0.5,lz:96.5,wx1:-12,wx2:12,wz1:84,wz2:108,bx1:-11,bx2:11,bz1:85,bz2:107,gx1:-10,gx2:10,gz1:86,gz2:106}
function mg:plot/build_one {n:5,lx:-36.5,lz:89.5,wx1:-49,wx2:-25,wz1:77,wz2:101,bx1:-48,bx2:-26,bz1:78,bz2:100,gx1:-47,gx2:-27,gz1:79,gz2:99}
function mg:plot/build_one {n:6,lx:-67.5,lz:68.5,wx1:-80,wx2:-56,wz1:56,wz2:80,bx1:-79,bx2:-57,bz1:57,bz2:79,gx1:-78,gx2:-58,gz1:58,gz2:78}
function mg:plot/build_one {n:7,lx:-88.5,lz:37.5,wx1:-101,wx2:-77,wz1:25,wz2:49,bx1:-100,bx2:-78,bz1:26,bz2:48,gx1:-99,gx2:-79,gz1:27,gz2:47}
function mg:plot/build_one {n:8,lx:-95.5,lz:0.5,wx1:-108,wx2:-84,wz1:-12,wz2:12,bx1:-107,bx2:-85,bz1:-11,bz2:11,gx1:-106,gx2:-86,gz1:-10,gz2:10}
function mg:plot/build_one {n:9,lx:-88.5,lz:-36.5,wx1:-101,wx2:-77,wz1:-49,wz2:-25,bx1:-100,bx2:-78,bz1:-48,bz2:-26,gx1:-99,gx2:-79,gz1:-47,gz2:-27}
function mg:plot/build_one {n:10,lx:-67.5,lz:-67.5,wx1:-80,wx2:-56,wz1:-80,wz2:-56,bx1:-79,bx2:-57,bz1:-79,bz2:-57,gx1:-78,gx2:-58,gz1:-78,gz2:-58}
function mg:plot/build_one {n:11,lx:-36.5,lz:-88.5,wx1:-49,wx2:-25,wz1:-101,wz2:-77,bx1:-48,bx2:-26,bz1:-100,bz2:-78,gx1:-47,gx2:-27,gz1:-99,gz2:-79}
function mg:plot/build_one {n:12,lx:0.5,lz:-95.5,wx1:-12,wx2:12,wz1:-108,wz2:-84,bx1:-11,bx2:11,bz1:-107,bz2:-85,gx1:-10,gx2:10,gz1:-106,gz2:-86}
function mg:plot/build_one {n:13,lx:37.5,lz:-88.5,wx1:25,wx2:49,wz1:-101,wz2:-77,bx1:26,bx2:48,bz1:-100,bz2:-78,gx1:27,gx2:47,gz1:-99,gz2:-79}
function mg:plot/build_one {n:14,lx:68.5,lz:-67.5,wx1:56,wx2:80,wz1:-80,wz2:-56,bx1:57,bx2:79,bz1:-79,bz2:-57,gx1:58,gx2:78,gz1:-78,gz2:-58}
function mg:plot/build_one {n:15,lx:89.5,lz:-36.5,wx1:77,wx2:101,wz1:-49,wz2:-25,bx1:78,bx2:100,bz1:-48,bz2:-26,gx1:79,gx2:99,gz1:-47,gz2:-27}
function mg:plot/forceload_remove
function mg:core/forceloads
tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Plots construits.","color":"green"}]
data modify storage mg:setup plot set value 1b
