"""Render a geographic opening from public-domain Natural Earth outlines.
Jakarta is the actual point plotted (106.8456 E, 6.2088 S).
Requires matplotlib. This is a geographic illustration, not an operating footprint.
"""
import argparse
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle
from matplotlib.font_manager import FontProperties

parser=argparse.ArgumentParser()
parser.add_argument("--output", default="/tmp/secha-indonesia-frames")
args=parser.parse_args()
output=Path(args.output)
output.mkdir(parents=True,exist_ok=True)
root=Path(__file__).resolve().parent
data=json.loads((root/"data/natural-earth-countries.geojson").read_text())
font=FontProperties(fname=str(root/"data/Inter-Variable.ttf"))
navy="#162638"
ivory="#f4efe4"
bronze="#c4a578"
for i in range(60):
    ratio=i/59
    fig=plt.figure(figsize=(9.6,5.4),dpi=100,facecolor=navy)
    ax=fig.add_axes([0,0,1,1],facecolor=navy)
    ax.set_xlim(65,151)
    ax.set_ylim(-17,56)
    ax.axis("off")
    for feature in data["features"]:
        geom=feature["geometry"]
        polygons=geom["coordinates"] if geom["type"]=="MultiPolygon" else [geom["coordinates"]]
        is_indonesia=feature["properties"]["name"]=="Indonesia"
        for polygon in polygons:
            ax.add_patch(Polygon(polygon[0],closed=True,
                facecolor=bronze if is_indonesia else "#263b51",
                edgecolor=bronze if is_indonesia else "#637385",linewidth=0.6,alpha=1))
    # Two expanding rings communicate origin and ambition, not city operations.
    for delay in [0,0.42]:
        phase=(ratio+delay)%1
        ax.add_patch(Circle((106.8456,-6.2088),radius=1+phase*13,
                            fill=False,edgecolor=bronze,linewidth=1.3,alpha=(1-phase)*.85))
    ax.scatter([106.8456],[-6.2088],s=38,c=ivory,zorder=10,edgecolors=bronze,linewidths=1.4)
    ax.text(105,-12,"JAKARTA  /  INDONESIA",fontproperties=font,fontsize=9,color=ivory,ha="center")
    ax.text(108,46,"ASIA",fontproperties=font,fontsize=18,color=ivory,ha="center",alpha=.9)
    ax.text(108,41.7,"ONE REPEATABLE SYSTEM",fontproperties=font,fontsize=8,color=bronze,ha="center")
    fig.savefig(output/f"{i:04d}.png",dpi=100,facecolor=navy,pad_inches=0)
    plt.close(fig)
print(f"Rendered 60 geographic frames to {output}")
