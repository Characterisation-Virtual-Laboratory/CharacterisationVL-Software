# CharacterisationVL-Software
The purpose of this repository is for storing definition files to submit to singularity hub.

Each software package is located in its own folder. The files are tagged with the software name and version number or date of build.

To add software to the repository you will need to create a new branch. The new branch will be checked and merged.

## Steps to add a software package
1. Create a branch
```
$ git branch <software name>
```
2. Make a subdirectory
3. Add all the necessary files
 * Singularity definition file or installation script
 * Readme file including install and testing notes
 * Desktop files for adding to menus with necessary tags
4. Commit all changes, including a helpful message
5. Check singularity hub for completed build.
```
$ git commit -m "<software name> added as requested in support ticket"
```
5. Submit merge request




[![https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg](https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg)](https://singularity-hub.org/collections/1396)
