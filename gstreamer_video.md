#### Gstreamer video comparison table
|    | Width | Height | Type| Encode| Mux | Framerate | Time (sec)| Size (KB) |CPU Load (capture) |CPU Load (record) |
|:--:|:-----:|:------:|:---:| :----:|:---:|:------:|:------:|:-----:|:-----:|:--:|
| 1 | 320   | 240 | avi | xvidenc | avimux  | 30  | 10 |  260 | 3% | 7% |
| 2 | 1280   | 720 | avi | xvidenc | avimux | 10 | 10 |   1100 | 4% | 20% |
| 3 | 1280   | 720 | mp4 | x264enc | mp4mux | 10 | 10 |   1208 | 4% | 45% |
| 4 | 1280   | 720 | mp4 | x264enc | mp4mux | 30 | 10 |   1304 | 5% | 78% |
| 5 | 320   | 240 | avi | x264enc | avimux | 30  | 10   |  1404| 3% | 13% |
| 6 | 1280   | 720 | flv | x264enc | flvmux | 10 | 10 |   1424 | 5% | 50% |
| 7 | 640   | 480 | avi | xvidenc | avimux  | 30  | 10 |  1456 | 4% | 12% |
| 8 | 1280   | 720 | avi | x264enc | avimux | 10  | 10 |   1576 | 5% | 52% |
| 9 | 640   | 480 | mp4 | x264enc | mp4mux  | 30  | 10 |  1600  | 4% | 12%|
| 10 | 1280   | 720 | flv | x264enc | flvmux | 30 | 10 |   1824 | 5% | 80% |
| 11 | 320   | 240 | mp4 | x264enc | mp4mux  | 30  | 10 |  1876 | 3% | 13% |
| 12 | 320   | 240 | flv | x264enc | flvmux  | 30  | 10 |  1940 | 3% | 13% |
| 13 | 640   | 480 | flv | x264enc | flvmux  | 30  | 10 |  1944 | 4% | 28% |
| 14 | 1280   | 720 | avi | x264enc | avimux | 30  | 10 | 1960 | 5% | 76% |
| 15 | 640   | 480 | avi | x264enc | avimux | 30  | 10 | 2020 | 4% | 29% |
| 16 | 1280   | 720 | avi | xvidenc | avimux | 30 | 10 |2620 | 5% | 79% |


#### Capture video with gstreamer
```
gst-launch --gst-plugin-path D:\ProgramFiles2\Python27\Lib\site-packages\gst-0.10\gst\plugins autovideosrc ! ffmpegcolorspace ! videoscale ! "video/x-raw-yuv, framerate=30/1, width=320, height=240" ! tee name=t1 t1. ! queue ! autovideosink
```

#### Record video with gstreamer
```
gst-launch --gst-plugin-path D:\ProgramFiles2\Python27\Lib\site-packages\gst-0.10\gst\plugins autovideosrc ! ffmpegcolorspace ! videoscale ! "video/x-raw-yuv, framerate=30/1, width=320, height=240" ! xvidenc ! queue ! mux. avimux name=mux ! filesink location=1.avi –v -e
```

#### Gstreamer container types
http://gstreamer.freedesktop.org/data/doc/gstreamer/head/pwg/html/section-types-definitions.html


#### Get available video modes
```python
from pygst_utils.video_source import get_available_video_modes
get_available_video_modes()
```
