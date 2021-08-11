# Nvidia-GPU-Acceleration-of-Azure-Custom-Vision-Models-for-AMD64
One of the biggest challenges in leveraging Azure's Custom Vision containers has been the lack of native GPU acceleration for the exported Tensorflow model when deploying to IoT Edge. The purpose of this repository is to share my learnings from experimenting with Nvidia GPU-based AMD64 devices, using IoT Edge with Azure Custom Vision containers.

After going through a large number of dockerfile build iterations, I found a new recipe which increases performance dramatically on Nvidia GPU-based devices while still preserving the convenience of Custom Vision.

Testing raw .jpg images with this build on a single Tesla T4 running Ubunutu 18.04

I hope that you find this useful for your Azure IoT Edge deployments!


