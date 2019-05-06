## Installation README

* Website:  
            https://www.rbvi.ucsf.edu/chimerax/

* Download:   
            https://www.rbvi.ucsf.edu/chimerax/download.html

* Licence:  
            https://www.rbvi.ucsf.edu/chimera/docs/licensing.html

* Prerequisites:
            ChimeraX is required to build this container. Please refer to Download above to obtain a copy of chimeraX.
            At the time of building the container, licensing does not support redistribution of the software.

            chimerax-0.8.tar.gz   - required for chimerax-v0.8.def
            chimerax-0.6.tar.gz   - required for chimerax-v0.6.def

* Run:      
            singularity exec --nv imageFileName.simg vglrun ChimeraX
