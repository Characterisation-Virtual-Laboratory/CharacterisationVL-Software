## Installation README

* Website:  
            https://www.electrontomography.org/
* Source:   
            The source code is not available on this website.

* Licence:  
            Copyright � 2012 Hanspeter Winkler

            Redistribution of source and binary code, with or without modification,
            are not permitted without specific prior written permission.

* Prerequisites:
            The following files are required to build this container:
            - protomo-2.4.2.tar.bz2
            - i3-0.9.8.tar.bz2
            Due to licensing requirements, you are required
            to create an account on the website (https://www.electrontomography.org/)
            to download the files.

* Run:      
            singularity exec imageFileName.simg tomocreatetlt.sh
            singularity exec imageFileName.simg tomoalign-gui
            singularity exec imageFileName.simg python

* Test:     
            Download "protomo-tutorial-2.4.2.tar.bz2" and extract it.
            The tutorial involves running some Protomo commands and then coding
            some python in a shell.

            Sample protomo commands used for testing:

            cd protomo-tutorial-2.4.2/singleaxis
          	rm max.i3t
          	tomocreatetlt.sh max.dat max 101 > max.tlt
          	tomoalign-gui -tlt max.tlt max.param
          	cp max.i3t maxsaved.i3t

            Use 'singularity shell containerName' to shell into the container.
            Start a python shell and then enter the following commands. If there
            is an issue importing protomo, the container hasn't built correctly.

        		import protomo
        		maxgeom = protomo.geom( "max.tlt" )
        		maxparam = protomo.param( "max.param" )
            max = protomo.series( maxparam )
        		zero = max.image( 120 )
        		zero.display()
        		zero = max.transform( 120 )
        		zero.display()
        		zero = max.filter( 120 )
        		zero.display()
        		max.align()
        		max.plot()
        		max.corr()
        		max.corr("out/max00.corr")


* Examples:
            Online tutorial: https://www.electrontomography.org/?page_id=345
