## Installation README

* Website:  
            https://pjreddie.com/darknet/
* Source:   
            https://github.com/AlexeyAB/darknet/tree/darknet_yolo_v3

* Licence:  
            Public Domain: https://github.com/AlexeyAB/darknet/blob/darknet_yolo_v3/LICENSE

* Run:      
            singularity exec --nv imageFileName.simg darknet detector

* Test:     
            singularity shell --nv imageFileName.simg
            cd /opt/darknet
            darknet detector test cfg/coco.data cfg/yolov3.cfg ~/yolov3.weights data/dog.jpg

* Examples:
            https://github.com/AlexeyAB/darknet/tree/darknet_yolo_v3
            The URL contains details on how to train and run darknet.
