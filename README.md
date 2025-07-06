
感谢原作者写的插件，fork修改了一下支持MPS

模型手动下载的话在这里下载：https://huggingface.co/lj1995/VoiceConversionWebUI/tree/main/uvr5_weights

下载后模型放到这里： ～/ComfyUI/custom_nodes/ComfyUI-UVR5/uvr5/uvr5_weights

Download with huggingface-cli:

``` bash
huggingface-cli download lj1995/VoiceConversionWebUI --include "uvr5_weights/*.*" --local-dir custom_nodes/ComfyUI-UVR5/uvr5
```

# ComfyUI-UVR5
the comfyui custom node for [UVR5](https://github.com/Anjok07/ultimatevocalremovergui) to separate vocals and background music
<div>
  <figure>
  <img alt='webpage' src="web.png?raw=true" width="600px"/>
  <figure>
</div>
    
## How to use
make sure `ffmpeg` is worked in your commandline
for Linux
```
apt update
apt install ffmpeg
```
for Windows,you can install `ffmpeg` by [WingetUI](https://github.com/marticliment/WingetUI) automatically

then!
```
git clone https://github.com/AIFSH/ComfyUI-UVR5.git
cd ComfyUI-UVR5
pip install -r requirements.txt
```
`weights` will be download from huggingface automatically!

## Windows
There is a portable standalone build for Windows that should work for running on Nvidia GPUs and cuda>=11.8,
click [the link](https://www.bilibili.com/video/BV1qx4y1h7T2) to download
<div>
  <figure>
  <img alt='Wechat' src="1key.jpg?raw=true" width="300px"/>
  <figure>
</div>

## Tutorial
- [demo](https://www.bilibili.com/video/BV1Tr421x75F/?share_source=copy_web&vd_source=453c36b4abef37acd389d4c01b149023)
- [FULL WorkFLOW](https://www.bilibili.com/video/BV1XE421T7ja)
## WeChat Group && Donate
<div>
  <figure>
  <img alt='Wechat' src="wechat.jpg?raw=true" width="300px"/>
  <img alt='donate' src="donate.jpg?raw=true" width="300px"/>
  <figure>
</div>

## Thanks
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS.git)
- [ultimatevocalremovergui](https://github.com/Anjok07/ultimatevocalremovergui) also konwn as UVR5

