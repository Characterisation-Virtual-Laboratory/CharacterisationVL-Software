## Installation README

* Website:  
            https://scipopt.org/index.php

* Source:   
            https://scipopt.org/index.php#download

* Licence:  
            https://scipopt.org/index.php#license

* Prerequisites:    
            To build this container fill out the license form and download the installer from:  
            https://scipopt.org/download.php?fname=SCIPOptSuite-7.0.3-Linux-ubuntu.sh  
            https://scipopt.org/download.php?fname=SCIPOptSuite-8.0.0-Linux-ubuntu.sh

* Run:      
            singularity exec \<image file name\>.sif scip  
            OR  
            singularity exec \<image file name\>.sif gcg  
            OR  
            singularity exec \<image file name\>.sif soplex \<file\>  
            OR  
            singularity exec \<image file name\>.sif zimpl \<file\>

* Test:     
            Place `simple.lp` in the mounted directory of the Singularity container  
            Refer to this for more info about mounted directories: https://stackoverflow.com/questions/66175271/singularity-sandbox-file-management  
            singularity exec \<image file name\>.sif scip -c "read simple.lp optimize quit"
            <p>
            Place `ex1.zpl` in the mounted directory of the Singularity container
            singularity exec \<image file name\>.sif zimpl ex1.zpl

* Examples:  
            https://www.scipopt.org/doc/html/index.php#QUICKSTART (included in this folder)  
            https://zimpl.zib.de/download/zimpl.pdf (page 4, included in this folder)  
            https://scipopt.org/doc/html/EXAMPLES.php
