from bokeh.io import curdoc
from bokeh.models.widgets import Tabs, Button
from bokeh.layouts import row, column

from scripts.core import core
from scripts.imageview import ImageView
from scripts.process import getImageData

import base64
from imageio import imread
import io
import matplotlib.pyplot as plt


# tab = core()
imgView = ImageView()
view = imgView.getView();

def callback():
    print imgView.getName()[:100]
    b64_string = imgView.getName()
    step1 = base64.b64decode(b64_string)
    # img = imread(io.BytesIO())
    # plt.figure()
    # plt.imshow(img, cmap="gray")



button = Button(label="Process...", )
button.on_click(callback);

# tabs = Tabs(tabs =[tab])
curdoc().add_root(row(view,button))
