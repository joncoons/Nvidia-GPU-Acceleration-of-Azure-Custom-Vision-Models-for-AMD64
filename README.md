# Nvidia GPU Acceleration of Azure Custom Vision models for AMD64
One of the challenges in leveraging Azure's Custom Vision containers for production has been GPU acceleration for the exported model when deploying to IoT Edge. The purpose of this repository is to share my learnings from experimenting with Nvidia GPU-based AMD64 devices, using IoT Edge with Azure Custom Vision containers.

After going through a large number of dockerfile iterations, I found a 'recipe' which increases performance dramatically on Nvidia GPU-based devices while still preserving the convenience of the Azure Custom Vision export. This repository builds off of the samples available at https://github.com/microsoft/onnxruntime.

Testing raw .jpg images over HTTP with this build on a single Nvidia Tesla T4 running Ubunutu 18.04 using a Flask app has been yielding results in the ~40ms range. Faster round-trip inference times could likely be achieved through utilizing gRCP endpoints in lieu of HTTP, which is a planned enhancement to the example.

To get started, go to https://azure.microsoft.com/en-us/services/cognitive-services/custom-vision-service/ and train your object detection model using Azure Custom Vision.  Export the trained model as an ONNX model (FP16 or FP32), and replace the model.onnx placeholder file in the folder above, as well as the labels.txt file.

If you're looking for a different ONNX runtime environment, please visit https://github.com/microsoft/onnxruntime/blob/master/dockerfiles/README.md to review the support matrix and docker pull tags.

I hope that you find this useful for your Azure IoT Edge deployments!


