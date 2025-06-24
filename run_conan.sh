#!/usr/bin/env bash

cd package1
conan create . --test-folder testpackage
cd -

cd package2
conan create . --test-folder testpackage
cd -