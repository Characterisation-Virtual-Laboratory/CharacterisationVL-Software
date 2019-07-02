## Installation README

* Website:  
            http://www.gatan.com/products/tem-analysis/gatan-microscopy-suite-software
* Source:   
            https://gatan.sharefile.com/share/view/sa9b5f88294f46ae9/fod776c2-8ec8-4492-acb9-3719cdf8a788
* Licence:  
            https://gatan.sharefile.com/share/view/sa9b5f88294f46ae9/fo127be3-01fb-4ec8-baac-0b886a8bb3e9
* Prerequesites:     
            The 32-bit Wine prefix has to be built first based on the source files (requires manual interaction during software installation and a few tweaks) and then copied into the container during the container build.
* Run:      
            WINEPREFIX=/opt/Wine32_free_prefix wine /opt/Wine32_free_prefix/drive_c/Program\ Files/Gatan/DigitalMicrograph.exe; however, this doesn't seem to work as a singularity exec command, which is why it was entered as the run command in the container recipe.
