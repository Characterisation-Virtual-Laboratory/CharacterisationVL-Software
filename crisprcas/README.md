## Installation README

* Website:  
            CRISPRCasFinder - https://crisprcas.i2bc.paris-saclay.fr/CrisprCasFinder/Index
            CRISPRCasViewer - https://crisprcas.i2bc.paris-saclay.fr/CrisprCasFinder/Viewer
* Source:   
            CRISPRCasFinder - https://crisprcas.i2bc.paris-saclay.fr/Home/DownloadFile?filename=CRISPRCasFinder.zip
            CRISPRCasViewer - https://crisprcas.i2bc.paris-saclay.fr/Home/DownloadFile?filename=CRISPRCasViewer.zip
            Manual          - https://crisprcas.i2bc.paris-saclay.fr/Home/DownloadFile?filename=CRISPRCasFinder_Viewer_manual.pdf

* Licence:  
            GPL v3. Please refer to COPYING and COPYRIGHT within the .zip file or /opt/CRISPRCasFinder within the container.

* Run:      
            CRISPRCasFinder - singularity exec containerFileName.simg perl /opt/CRISPRCasFinder/CRISPRCasFinder.pl
            CRISPRCasViewer - singularity exec containerFileName.simg firefox /opt/CRISPRCasViewer/CRISPRCasViewer.html

* Test:     
            CRISPRCasFinder:

            	Ensure Finder is run from a writeable folder. 

            	cd ~
            	singularity exec containerFileName.simg perl /opt/CRISPRCasFinder/CRISPRCasFinder.pl -cf CasFinder-2.0.2 -def General -cas -i /opt/CRISPRCasFinder/install_test/sequence.fasta -out ~/Results_test_install -keep -soFile /opt/CRISPRCasFinder/sel392v2.so
            	diff ~/Results_test_install/TSV/Cas_REPORT.tsv /opt/CRISPRCasFinder/install_test/Cas_REPORT.tsv
            	diff ~/Results_test_install/TSV/Crisprs_REPORT.tsv /opt/CRISPRCasFinder/install_test/Crisprs_REPORT.tsv
            
            	There may be minor differences according to the user manual.

            CRISPRCasViewer:
            
           	singularity exec containerFileName.simg firefox /opt/CRISPRCasViewer/CRISPRCasViewer.html

* Examples:
            Please refer to the Manual or view CRISPCasFinder help for information
            singularity exec containerFileName.simg perl /opt/CRISPRCasFinder/CRISPRCasFinder.pl -help
