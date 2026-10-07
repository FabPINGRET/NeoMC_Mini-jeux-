"""Musiques du kart (compositions originales, façon jeu de course) jouées en blocs musicaux : python gen_music.py ../../data/mg

Chaque morceau fait 128 croches (16 mesures, structure A A' B A'') ; une croche toutes les 4 ticks (3 au dernier tour).
  t1 : Circuit Champignon (ré majeur, entraînant)      t2 : Royaume Koopa (mi dorien, aventure)
  t3 : Bataille (la mineur, tendu)                      star : étoile d'invincibilité (boucle de 32 croches)
Sortie : data/mg/function/kart/mus/<morceau>_<n>.mcfunction, joués pour @s (catégorie « record » : réglable avec le volume Juke-box).
"""
import os, random, sys

OUT = os.path.join(sys.argv[1], 'function', 'kart', 'mus')
os.makedirs(OUT, exist_ok=True)
for f in os.listdir(OUT):
    os.remove(os.path.join(OUT, f))

def pitch(midi, inst):
    """hauteur Minecraft (0,5 à 2) ; la basse sonne deux octaves sous la harpe."""
    m = midi + (24 if inst in ('bass', 'didgeridoo') else 0)
    while m < 54: m += 12
    while m > 78: m -= 12
    return round(2 ** ((m - 66) / 12), 4)

SCALES = {'major': [0, 2, 4, 5, 7, 9, 11], 'dorian': [0, 2, 3, 5, 7, 9, 10], 'minor': [0, 2, 3, 5, 7, 8, 10]}
RHYTHMS = [  # 16 croches (2 mesures) : 1 = note, 0 = silence, 2 = tenue
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 2, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 2, 2, 0, 1, 1, 1, 0],
    [1, 2, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 2, 2, 0],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 2, 2, 2],
]

def compose(seed, root, scale, prog_a, prog_b, inst, steps=128):
    rnd = random.Random(seed)
    sc = SCALES[scale]
    def degree_midi(deg, base):
        o, d = divmod(deg, 7)
        return base + 12 * o + sc[d]
    def chord_tones(ch):                       # degrés de l'accord (fondamentale, tierce, quinte)
        return [ch, ch + 2, ch + 4]
    events = [[] for _ in range(steps)]
    def phrase(prog, rhythm, start_deg, vary):
        notes, deg = [], start_deg
        for i, r in enumerate(rhythm):
            ch = prog[i // 8]
            if r == 1:
                if i % 4 == 0:
                    tones = chord_tones(ch)
                    deg = min(tones + [t + 7 for t in tones], key=lambda t: abs(t - deg) + rnd.random() * 1.5)
                else:
                    deg += rnd.choice([-1, -1, 1, 1, 2, -2, 0])
                deg = max(4, min(15, deg))
                if vary and i >= 12: deg += rnd.choice([0, 1, 2])
                notes.append(deg)
            else:
                notes.append(None if r == 0 else 'hold')
        return notes
    sections = []
    ra, rb = rnd.choice(RHYTHMS), rnd.choice(RHYTHMS)
    pa = phrase(prog_a[0:2], ra, 7, False) + phrase(prog_a[2:4], ra, 9, False)
    pa2 = pa[:16] + phrase(prog_a[2:4], rb, 9, True)
    pb = phrase(prog_b[0:2], rb, 9, False) + phrase(prog_b[2:4], rb, 11, True)
    for sec, prog in ((pa, prog_a), (pa2, prog_a), (pb, prog_b), (pa2, prog_a)):
        sections.append((sec, prog))
    base = root
    for s, (mel, prog) in enumerate(sections):
        for i in range(32):
            st = s * 32 + i
            if st >= steps: break
            bar = i // 8
            ch = prog[bar]
            n = mel[i]
            if isinstance(n, int):
                events[st].append((inst['lead'], pitch(degree_midi(n, base), inst['lead']), 0.5))
                if s == 2 and inst.get('echo'):
                    events[st].append((inst['echo'], pitch(degree_midi(n, base) + 12, inst['echo']), 0.2))
            # basse : fondamentale, fondamentale, quinte, octave
            bdeg = [ch, ch, ch + 4, ch + 7][(i % 8) // 2] if i % 2 == 0 else None
            if bdeg is not None:
                events[st].append((inst['bass'], pitch(degree_midi(bdeg, base - 24), inst['bass']), 0.55))
            # arpège léger dans la partie B
            if s == 2 and inst.get('arp') and i % 2 == 1:
                events[st].append((inst['arp'], pitch(degree_midi(chord_tones(ch)[(i // 2) % 3] + 7, base), inst['arp']), 0.22))
            # batterie
            if i % 4 == 0: events[st].append(('basedrum', 0.8, 0.5))
            if i % 4 == 2: events[st].append(('snare', 1.0, 0.35))
            events[st].append(('hat', 1.6 if i % 2 else 1.3, 0.13))
            if inst.get('fill') and i % 32 in (29, 30, 31): events[st].append(('snare', 1.3, 0.3))
    return events

def write_track(name, events):
    for st, ev in enumerate(events):
        lines = [f'playsound minecraft:block.note_block.{ins} record @s ~ ~ ~ {vol} {p}' for ins, p, vol in ev]
        with open(os.path.join(OUT, f'{name}_{st}.mcfunction'), 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(lines or ['# silence']) + '\n')

# progressions en degrés (0 = I)
write_track('t1', compose(61, 62, 'major', [0, 5, 3, 4], [3, 4, 2, 5], {'lead': 'bit', 'bass': 'bass', 'arp': 'bell', 'echo': 'chime', 'fill': True}))
write_track('t2', compose(62, 64, 'dorian', [0, 6, 5, 6], [3, 4, 0, 6], {'lead': 'flute', 'bass': 'bass', 'arp': 'pling', 'echo': 'bell', 'fill': True}))
write_track('t3', compose(63, 57, 'minor', [0, 5, 6, 0], [3, 4, 5, 4], {'lead': 'pling', 'bass': 'didgeridoo', 'arp': 'bit', 'fill': True}))
# étoile : arpèges rapides et cloche, 32 croches en boucle
star = [[] for _ in range(128)]
for st in range(128):
    i = st % 32
    tones = [62, 66, 69, 74, 78, 74, 69, 66]
    star[st].append(('bit', pitch(tones[i % 8] + (2 if (i // 8) % 2 else 0), 'bit'), 0.45))
    if i % 2 == 0: star[st].append(('bass', pitch(38 + (2 if (i // 8) % 2 else 0), 'bass'), 0.5))
    if i % 4 == 0: star[st].append(('basedrum', 0.8, 0.5))
    if i % 4 == 2: star[st].append(('cow_bell', 1.2, 0.35))
    star[st].append(('hat', 1.7, 0.15))
write_track('star', star)
print('musiques : 4 x 128 croches')
