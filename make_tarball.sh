#!/bin/sh

tar cvzf releases/adoptopenjdk-repo-$1.tar.gz --exclude ".DS_Store" adoptopenjdk-repo-$1
