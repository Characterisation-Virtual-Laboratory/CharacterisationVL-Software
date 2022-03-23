#!/bin/bash

# Build-A-Branch
#
# This script is meant to be executed as part of a GitHub action.
# It will build a Singularity container from a new recipe pushed to the repo
#
# Assumptions:
# You are running this script from the base of the repository.
# You have checked out the new app's branch and pulled it.


# Preserve starting directory in case of multiple builds in one commit
# TODO: Make the container and log directories input arguments
BASEDIR=$PWD
CONTAINERDIR="/mnt/volume/test-containers"
LOGDIR="/mnt/volume/logs"

# Find out new and changed files via git diff-tree
for FILE in `git diff-tree --no-commit-id --name-only`
do
	FILENAME=basename($FILE)
	# Only operate on Singularity recipes, adopting the convention that they are all named "Singularity.appname"
	if [[ $FILENAME =~ '^Singularity\.' ]]
	then
		# Call the resulting container and log the same as the app name
		CONTAINERNAME=${$FILE#Singularity.}
		cd dirname($FILE)
		# TODO: consider the security implications of not restricting commands in sudoers or setuid the script
		sudo singularity build $CONTAINERDIR/$CONTAINERNAME.sif 2>&1 > $LOGDIR/$CONTAINERNAME.log
		# Return to the repo's base directory to potentially build the next recipe
		cd $BASEDIR
	fi
done
