#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
NS3DIR=$DIR/ns-3
cd $NS3DIR > /dev/null
./waf configure --build-profile=optimized --disable-werror