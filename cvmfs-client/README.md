## Installation README

Custom Build of CVMFS Client based on Opensciencegrid.org Config

* Website:  
            https://cernvm.cern.ch/fs/
* Source:   
	    https://cernvm.cern.ch/fs/
* Licence:  
            BSD 3-Clause "New" or "Revised" License
* Run:      
            CONFIGREPO=config-osg.opensciencegrid.org
            CACHEDIR=/tmp/$USER/cvmfs_cache
            mkdir -p $CACHEDIR
            singularity shell -S /var/run/cvmfs -B $CACHEDIR:/var/lib/cvmfs --fusemount "container:cvmfs2 $CONFIGREPO /cvmfs/$CONFIGREPO" --fusemount "container:cvmfs2 cms.cern.ch /cvmfs/cms.cern.ch" imageFileName.sif
* Test:     
            CONFIGREPO=config-osg.opensciencegrid.org
            CACHEDIR=/tmp/$USER/cvmfs_cache
            mkdir -p $CACHEDIR
            singularity exec -S /var/run/cvmfs -B $CACHEDIR:/var/lib/cvmfs --fusemount "container:cvmfs2 $CONFIGREPO /cvmfs/$CONFIGREPO" --fusemount "container:cvmfs2 cms.cern.ch /cvmfs/cms.cern.ch" imageFileName.sif ls /cvmfs/
