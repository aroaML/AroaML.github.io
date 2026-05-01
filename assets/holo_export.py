import math, os
from PIL import Image
import numpy as np

W, H          = 600, 380
FPS           = 30
DURATION      = 9.0   # full cycle (9s = one loop of the CSS animation)
TOTAL_FRAMES  = int(FPS * DURATION)
OUT_PATH      = os.path.join(os.path.dirname(__file__), "holo-shift.gif")

STOPS = [
    (0.00, 0x4A, 0x32, 0x60),
    (0.60, 0x6A, 0xA8, 0xA4),
    (1.00, 0x8A, 0x6E, 0x9A),
]

def lerp_stops(t):
    for i in range(len(STOPS) - 1):
        p0, r0, g0, b0 = STOPS[i]
        p1, r1, g1, b1 = STOPS[i + 1]
        if p0 <= t <= p1:
            f = (t - p0) / (p1 - p0)
            return int(r0 + (r1-r0)*f), int(g0 + (g1-g0)*f), int(b0 + (b1-b0)*f)
    return STOPS[-1][1], STOPS[-1][2], STOPS[-1][3]

def ease_in_out(t):
    return t * t * (3 - 2 * t)

def make_frame(bg_x):
    angle = math.radians(145)
    xs = (np.arange(W) / W) - 0.5
    ys = (np.arange(H) / H) - 0.5
    xg, yg = np.meshgrid(xs, ys)
    proj = xg * math.cos(angle) + yg * math.sin(angle)
    proj = (proj - proj.min()) / (proj.max() - proj.min())
    t_map = np.clip(proj * 0.5 + bg_x * 0.5, 0, 1)

    r = np.zeros((H, W), dtype=np.float32)
    g = np.zeros((H, W), dtype=np.float32)
    b = np.zeros((H, W), dtype=np.float32)
    for i in range(len(STOPS) - 1):
        p0, r0, g0_, b0 = STOPS[i]
        p1, r1, g1_, b1 = STOPS[i + 1]
        mask = (t_map >= p0) & (t_map <= p1)
        f = np.where(mask, (t_map - p0) / (p1 - p0), 0)
        r += mask * (r0 + (r1 - r0) * f)
        g += mask * (g0_ + (g1_ - g0_) * f)
        b += mask * (b0 + (b1 - b0) * f)

    img = np.stack([r, g, b], axis=2)
    # dark veil rgba(14,13,11,0.12)
    veil = np.array([14, 13, 11], dtype=np.float32) * 0.12
    img = np.clip(img * 0.88 + veil, 0, 255).astype(np.uint8)
    return img

print(f"Rendering {TOTAL_FRAMES} frames...")
frames = []
for f in range(TOTAL_FRAMES):
    cycle_t = f / TOTAL_FRAMES   # 0 → 1 over full 9s cycle
    if cycle_t < 0.5:
        bg_x = ease_in_out(cycle_t * 2)
    else:
        bg_x = ease_in_out((1 - cycle_t) * 2)
    frames.append(Image.fromarray(make_frame(bg_x)))

frame_ms = int(1000 / FPS)
palette_frames = [fr.convert("P", palette=Image.ADAPTIVE, colors=256, dither=Image.Dither.FLOYDSTEINBERG) for fr in frames]
palette_frames[0].save(OUT_PATH, save_all=True, append_images=palette_frames[1:], duration=frame_ms, loop=0, optimize=False)
print(f"Done: {OUT_PATH}")
