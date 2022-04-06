## Installation README

* Website:  
            https://docs.globus.org/how-to/globus-connect-personal-linux/
            https://downloads.globus.org/globus-connect-personal/linux/stable/globusconnectpersonal-latest.tgz

* Licence:  
            http://www.apache.org/licenses/LICENSE-2.0

* Run:      
            singularity exec imageFileName.simg globusconnectpersonal

* Test:     
            singularity exec imageFileName.simg globusconnectpersonal

* Examples:
            When Globus Connect Personal is initially executed, it will configure itself.
            You will need to login to Globus.org to complete the installation.

            Ensure you bind any local drives/folders when running otherwise, you may
            have difficulty accessing some paths.

            e.g. singularity exec -B /scratch:/scratch -B /projects:/projects imageFileName.simg globusconnectpersonal
