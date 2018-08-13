# Software installations tips and tricks


To replace text with sed you can use this example as a template
```
$ pwd > pathtest.txt
$ cat pathtest.txt
/scratch/pMOSP/lancew/CVL-singularity-repo/CharacterisationVL-Software
$ cat pathtest.txt |sed 's/\/lancew\//\/billybob\//g'
/scratch/pMOSP/billybob/CVL-singularity-repo/CharacterisationVL-Software
```
To replace text in a file
```
sed -i 's/\/lancew\//\/billybob\//g' pathtest.txt
```
