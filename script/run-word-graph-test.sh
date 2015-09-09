#!/bin/sh

# I am so dumb.

PYTHON=python

SRC_DIR=src
TEST_DIR=test
BUILD_DIR=build

TEST_NAME=WordGraphTest.py

if [ $(basename $PWD) != WordLadder ]; then
    echo "Must execute this script from the root of WordLadder."
    exit 1
fi

if [ ! -d $BUILD_DIR ]; then
    mkdir $BUILD_DIR
fi

cp $SRC_DIR/*.py $BUILD_DIR
cp $TEST_DIR/*.py $BUILD_DIR

cd $BUILD_DIR
$PYTHON $TEST_NAME
