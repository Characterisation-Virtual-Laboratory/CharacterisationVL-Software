## Installation README

* Website:  
            http://www.ccpem.ac.uk/download.php

* Source:   
            http://www.ccpem.ac.uk/downloads/ccpem_distributions/ccpem-1.3.0-linux-x86_64.tar.gz

* Licence:  
            http://www.ccpem.ac.uk/licensing/
            Please follow the licensing details and download ccp-em.

* Prerequisites:
            To build this container the following software is required:
            
            - CCP-EM - http://www.ccpem.ac.uk/downloads/ccpem_distributions/ccpem-1.3.0-linux-x86_64.tar.gz
                        - to deploy CCP-EM, a Modeller licence key is required (free for academic use). 
                        - Please follow the link on the CCP-EM downloads page for further details. 
                        - Once the key has been obtained edit the file 'input.txt' and replace the line 'MODELLER-KEY-GOES-HERE' with the key.
                        
            - CCP4   - http://www.ccp4.ac.uk/download/#os=linux 
                       - The container was originally constructed with CCP4 version 'ccp4-7.0.072-shelx-arpwarp-linux64.tar.gz'. 
                       - Archives of CCP4 are not available from this site. 
                       - You may need to edit the '%files' and '%post' section in the recipe file 'ccp-em_v1.3.0-cuda-9.0.def' to update the name of the CCP file.
            
            Place all files in the same folder as the recipe file (ccp-em_v1.3.0-cuda-9.0.def).
            To build the container: sudo singularity build ccpm.simg ccp-em_v1.3.0-cuda-9.0.def

* Run:      
            singularity exec --nv imageFileName.simg vglrun ccpem
            singularity exec --nv imageFileName.simg vglrun relion

* Test:     
            singularity exec --nv imageFileName.simg vglrun ccpem
