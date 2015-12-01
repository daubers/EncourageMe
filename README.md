# Login Encourager!

Provides you with some encouragement when you login

# Requirements

Requires Kivy
You may also need to alter the .sh to point at the correct venv/python environment :)


In order to install Kivy in a python environment on OSX first

brew install sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer

Then activate the venv

pip install -I Cython==0.21.2

and finally

USE_OSX_FRAMEWORKS=0 pip install git+https://github.com/kivy/kivy.git@1.9.0

Then just

python EncourageMe.py

penguin.gif from http://chibird.com/post/35377784683/a-little-penguin-encouragement-to-support-you-when who is an awesome artist and you should totally buy a shirt or donate some money by patreon or something