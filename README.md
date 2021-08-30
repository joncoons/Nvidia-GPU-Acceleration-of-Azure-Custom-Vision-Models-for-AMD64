# Nvidia-GPU-Acceleration-of-Azure-Custom-Vision-Models-for-AMD64
One of the biggest challenges in leveraging Azure's Custom Vision containers has been GPU acceleration for the exported model when deploying to IoT Edge. The purpose of this repository is to share my learnings from experimenting with Nvidia GPU-based AMD64 devices, using IoT Edge with Azure Custom Vision containers.

After going through a large number of dockerfile iterations, I found a 'recipe' which increases performance dramatically on Nvidia GPU-based devices while still preserving the convenience of the Azure Custom Vision export.

Testing raw .jpg images over HTTP with this build on a single Tesla T4 running Ubunutu 18.04 using a Flask app has been yielding results in the ~40ms range.

I hope that you find this useful for your Azure IoT Edge deployments!


