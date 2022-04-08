# kitTools
A small collection of weird gizmos I've made for Nuke.

### kitLUTLoader
Useful for applying LUTs to your scene. Wrapper for the Vectorfield node for ease of use. Includes luma / chroma and a mix slider.

### kitRGBInvert
Inverts an image in sRGB gamma rather than linear, gives slightly different results.

### kitInvReinhard & kitReinhard
Applies an inverse Reinhard tonemap to the input, boosting original values that approach 1 to pretty extreme luminance values. Useful for nicer bokeh highlights, glints & glows, whatever effect that benefits from HDR inputs. 

### kitDeflicker
A simple deflicker based off [this video](https://www.youtube.com/watch?v=Qxp7jjDhQWY). Modified so it only affects scene luminance and should avoid saturation / color shifts from exposure changes.
