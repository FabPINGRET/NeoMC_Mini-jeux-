"""🗺 Cartes supplémentaires des jeux d'arcade : relance chaque générateur avec d'autres réglages (voir common.py, NEOMC_MAP).

    python tools/arcade/gen_maps.py .

Chaque carte est un « clone » du jeu avec son propre id (200..213), son propre dossier de fonctions et sa zone, chargée
(forceload) seulement pendant la partie. Choix de la carte : menu ≡ → 🕹 Arcade → le jeu ▸ (tools/variantes/gen_variants.py).
"""
import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')   # sortie console en UTF-8 (Windows : cp1252 sinon)
R = sys.argv[1] if len(sys.argv) > 1 else '.'
HERE = os.path.dirname(os.path.abspath(__file__))

LABO = {'stone_bricks': 'white_concrete', 'cracked_stone_bricks': 'light_gray_concrete', 'polished_andesite': 'smooth_quartz',
        'mossy_stone_bricks': 'white_terracotta', 'polished_deepslate': 'polished_diorite', 'smooth_stone': 'white_concrete',
        'stone': 'smooth_stone', 'dark_oak_planks': 'iron_block', 'spruce_slab': 'smooth_quartz_slab',
        'spruce_planks': 'quartz_block', 'iron_bars': 'iron_bars'}
MANOIR = {'stone_bricks': 'deepslate_bricks', 'cracked_stone_bricks': 'cracked_deepslate_bricks', 'polished_andesite': 'spruce_planks',
          'mossy_stone_bricks': 'dark_oak_planks', 'polished_deepslate': 'red_nether_bricks', 'smooth_stone': 'dark_oak_planks',
          'stone': 'deepslate', 'dark_oak_planks': 'stripped_dark_oak_log', 'sea_lantern': 'shroomlight', 
          'spruce_slab': 'dark_oak_slab', 'spruce_planks': 'dark_oak_planks', 'soul_lantern': 'soul_lantern'}

MAPS = [
    ('gen_tron.py', dict(sfx='xl', keys=['tron'], ids={'84': 200, '85': 201}, entry='tron', label='XXL',
                         p=dict(Z=34000, H=100))),
    ('gen_survival.py', dict(sfx='2', keys=['survival', 'uhc', 'hg'], ids={'94': 202, '95': 203}, entry='survival', label='',
                             labels={'94': 'Désert', '95': 'Jungle'},
                             p=dict(ZU=34400, ZH=34600, seed_uhc=9411, seed_hg=9512, uhc_theme='desert', hg_theme='jungle'))),
    ('gen_survival.py', dict(sfx='3', keys=['survival', 'uhc', 'hg'], ids={'94': 204, '95': 205}, entry='survival', label='',
                             labels={'94': 'Taïga enneigée', '95': 'Canyon'},
                             p=dict(ZU=34800, ZH=35000, seed_uhc=9421, seed_hg=9522, uhc_theme='taiga', hg_theme='mesa'))),
    ('gen_koth.py', dict(sfx='2', keys=['koth'], ids={'86': 206, '87': 207}, entry='koth', label='Pyramide',
                         p=dict(Z=35300, ground=['sandstone', 'sand'], stairs='sandstone_stairs', cover='cut_sandstone', light='lantern',
                                tiers=['sandstone', 'cut_sandstone', 'smooth_sandstone', 'chiseled_sandstone', 'smooth_sandstone'],
                                title='pyramide de grès, sommet en or'))),
    ('gen_koth.py', dict(sfx='3', keys=['koth'], ids={'86': 208, '87': 209}, entry='koth', label='Glacier',
                         p=dict(Z=35500, ground=['snow_block', 'snow_block'], stairs='polished_diorite_stairs', cover='packed_ice',
                                light='sea_lantern', tiers=['packed_ice', 'blue_ice', 'packed_ice', 'snow_block', 'polished_diorite'],
                                title='colline de glace (ça glisse), sommet en or'))),
    ('gen_zombies.py', dict(sfx='2', keys=['zmode', 'zm', 'inf'], ids={'97': 210, '98': 211}, entry='zmode', label='Laboratoire',
                            p=dict(Z=35800, blocks=LABO, name='Laboratoire'))),
    ('gen_zombies.py', dict(sfx='3', keys=['zmode', 'zm', 'inf'], ids={'97': 212, '98': 213}, entry='zmode', label='Manoir',
                            p=dict(Z=36100, blocks=MANOIR, name='Manoir'))),
    ('gen_zombies.py', dict(sfx='4', keys=['zmode', 'zm', 'inf'], ids={'97': 229, '98': 230}, entry='zmode', label='Usine',
                            p=dict(Z=39100, layout='usine', name='Usine'))),
    ('gen_zombies.py', dict(sfx='5', keys=['zmode', 'zm', 'inf'], ids={'97': 231, '98': 232}, entry='zmode', label='Station',
                            p=dict(Z=39400, layout='station', name='Station'))),
    ('gen_ctf.py', dict(sfx='2', keys=['ctf'], ids={'93': 242}, entry='ctf', label='Nether',
                        p=dict(Z=41400, theme='nether', name='Nether'))),
    ('gen_ctf.py', dict(sfx='3', keys=['ctf'], ids={'93': 243}, entry='ctf', label='Banquise',
                        p=dict(Z=41500, theme='neige', name='Banquise'))),
    ('gen_zombies.py', dict(sfx='6', keys=['zmode', 'zm', 'inf'], ids={'97': 235, '98': 236}, entry='zmode', label='Hôpital',
                            p=dict(Z=39800, layout='hopital', name='Hôpital'))),
    ('gen_zombies.py', dict(sfx='7', keys=['zmode', 'zm', 'inf'], ids={'97': 237, '98': 238}, entry='zmode', label='Mine',
                            p=dict(Z=40200, layout='mine', name='Mine'))),
]
for script, cfg in MAPS:
    env = dict(os.environ, NEOMC_MAP=json.dumps(cfg, ensure_ascii=False))
    out = subprocess.run([sys.executable, os.path.join(HERE, script), R], env=env, capture_output=True, text=True)
    if out.returncode:
        sys.exit(out.stdout + out.stderr)
    print(f'{script} → {"/".join(k + cfg["sfx"] for k in cfg["keys"])} : ids {sorted(cfg["ids"].values())}')

# ids des cartes acceptés par core/go (1..N)
import re
_p = os.path.join(R, 'data/mg/function/core/go.mcfunction')
_t = open(_p, encoding='utf-8').read()
_hi = max(max(c['ids'].values()) for _, c in MAPS)
_m = re.search(r'unless score @s mg\.go matches 1\.\.(\d+) unless', _t)
if _m and int(_m.group(1)) < _hi:
    open(_p, 'w', encoding='utf-8', newline='\n').write(_t.replace(_m.group(0), f'unless score @s mg.go matches 1..{_hi} unless'))
