#!/bin/sh
#7557798583
mkdir ../outputs/Test1/
mkdir ../outputs/Test1/Markdown
bsub -o "../outputs/Test1/Markdown/Test1_0.md" -J "Test1_0" -env MYARGS="-name Test1-0 -GPU False -time 3600 -b 4.0 -a 1 -d dsf -ID 0" < submit_cpu.sh
mkdir ../outputs/Test2/
mkdir ../outputs/Test2/Markdown
bsub -o "../outputs/Test2/Markdown/Test2_0.md" -J "Test2_0" -env MYARGS="-name Test2-0 -GPU False -time 3600 -b 4.0 -a 1 -d dsf -ID 0" < submit_cpu.sh
