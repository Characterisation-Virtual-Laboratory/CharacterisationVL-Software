## Installation README

* Website:  
            https://scipopt.org/index.php

* Source:   
            https://scipopt.org/index.php#download

* Licence:  
            https://scipopt.org/index.php#license

* Prerequisites:
            <br>
            To build this container fill out the license form and download the installer from:
            <br>
            https://scipopt.org/download.php?fname=SCIPOptSuite-7.0.3-Linux-ubuntu.sh

* Run:      
            singularity exec \<image file name\>.sif scip

* Test:     
            Place `simple.lp` in the mounted directory of the Singularity container
            <br>
            Refer to this for more info about mounted directories: https://stackoverflow.com/questions/66175271/singularity-sandbox-file-management
            <br>
            singularity exec \<image file name\>.sif scip -c "read simple.lp optimize quit"

* Examples:
            <br>
            https://www.scipopt.org/doc/html/index.php#QUICKSTART (included in this folder)
            <br>
            https://scipopt.org/doc/html/EXAMPLES.php
