import matplotlib.pyplot as plt
from mplsoccer import VerticalPitch,Pitch,add_image,FontManager
from PIL import Image
from highlight_text import ax_text
from urllib.request import urlopen
import pandas as pd

pd.read_csv("messihm.csv")

pitch = VerticalPitch()
fig, axs = pitch.grid(figheight=15, ncols=3)