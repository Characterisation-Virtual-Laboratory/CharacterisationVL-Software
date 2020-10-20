#!/bin/bash
echo "Number of software packages"
find . -maxdepth 1 -type d |sort -u |grep "./" |grep -v 'xdg\|template' |wc -l
