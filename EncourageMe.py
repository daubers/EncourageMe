'''
Basic Picture Viewer
====================

This simple image browser demonstrates the scatter widget. You should
see three framed photographs on a background. You can click and drag
the photos around, or multi-touch to drop a red dot to scale and rotate the
photos.

The photos are loaded from the local images directory, while the background
picture is from the data shipped with kivy in kivy/data/images/background.jpg.
The file pictures.kv describes the interface and the file shadow32.png is
the border to make the images look like framed photographs. Finally,
the file android.txt is used to package the application for use with the
Kivy Launcher Android application.

For Android devices, you can copy/paste this directory into
/sdcard/kivy/pictures on your Android device.

The images in the image directory are from the Internet Archive,
`https://archive.org/details/PublicDomainImages`, and are in the public
domain.

'''

import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.logger import Logger
from kivy.uix.image import Image
from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')
import os

localpath=os.path.dirname(os.path.realpath(__file__))

class PicturesApp(App):

    def build(self):
        return Image(source=os.path.join(localpath,"penguin.gif"))


if __name__ == '__main__':
    PicturesApp().run()