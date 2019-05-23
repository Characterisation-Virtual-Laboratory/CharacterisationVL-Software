## Installation README

* Website:  
            https://libertem.github.io/LiberTEM/

* Source:   
            https://github.com/LiberTEM/LiberTEM

* Licence:  
            GPL v3 - https://github.com/LiberTEM/LiberTEM/blob/master/LICENSE

* Run:      
            singularity exec imageFileName.simg libertem-server --local_directory=$HOME/dask-worker-space

            Using your favourite web browser connect to: http://localhost:9000 
            Note: --local_directory must be set to a writable directory.

* Notes:
           The current version of LiberTEM is built from a fork which contains fixes to allow the 'local_directory' for Dask Distributed to be set to outside of the container. e.g. "$HOME/dask-worker-space" Prior to this change, the current working directory was used, which is read-only in a container deployment. This prevented LiberTEM from running.
