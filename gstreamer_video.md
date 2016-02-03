#### Gstreamer video comparison table
|    | Width | Height | Type| Encode| Mux | Framerate | Time (sec)| Size (KB) |
|:--:|:-----:|:------:|:---:| :----:|:---:|:---------:|----------:|----------:|
| 1 | 320   | 240 | avi | xvidenc | avimux  | 30  | 10 |  260     |
| 2 | 1280   | 720 | avi | xvidenc | avimux | 10 | 10 |   1100    |
| 3 | 1280   | 720 | mp4 | x264enc | mp4mux | 10 | 10 |   1208    |
| 4 | 1280   | 720 | mp4 | x264enc | mp4mux | 30 | 10 |   1304    |
| 5 | 320   | 240 | avi | x264enc | avimux | 30  | 10   |  1404     |
| 6 | 1280   | 720 | flv | x264enc | flvmux | 10 | 10 |   1424    |
| 7 | 640   | 480 | avi | xvidenc | avimux  | 30  | 10 |  1456     |
| 8 | 1280   | 720 | avi | x264enc | avimux | 10  | 10 |   1576    |
| 9 | 640   | 480 | mp4 | x264enc | mp4mux  | 30  | 10 |  1600     |
| 10 | 1280   | 720 | flv | x264enc | flvmux | 30 | 10 |   1824    |
| 11 | 320   | 240 | mp4 | x264enc | mp4mux  | 30  | 10 |  1876     |
| 12 | 320   | 240 | flv | x264enc | flvmux  | 30  | 10 |  1940     |
| 13 | 640   | 480 | flv | x264enc | flvmux  | 30  | 10 |  1944     |
| 14 | 1280   | 720 | avi | x264enc | avimux | 30  | 10 |   1960    |
| 15 | 640   | 480 | avi | x264enc | avimux | 30  | 10 |  2020     |
| 16 | 1280   | 720 | avi | xvidenc | avimux | 30 | 10 |   2620    |

#### Gstreamer container types
http://gstreamer.freedesktop.org/data/doc/gstreamer/head/pwg/html/section-types-definitions.html

#### Get available video modes
```python
from pygst_utils.video_source import get_available_video_modes
get_available_video_modes()
```
