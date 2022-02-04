#!/bin/sh
#4030106945
mkdir ../outputs/Test1/
mkdir ../outputs/Test1/Markdown
bsub -o "../outputs/Test1/Markdown/Test1_0.md" -J "Test1_0" -env MYARGS="-name Test1-0 -GPU False -time 3600 -b 4.0 -a 1 -d dsf -ID 0" < submit_cpu.sh
mkdir ../outputs/Test2/
mkdir ../outputs/Test2/Markdown
bsub -o "../outputs/Test2/Markdown/Test2_0.md" -J "Test2_0" -env MYARGS="-name Test2-0 -GPU True -time 3600 -b 4.0 -a 1 -d dssf -ID 0" < submit_gpu.sh
mkdir ../outputs/Test3/
mkdir ../outputs/Test3/Markdown
bsub -o "../outputs/Test3/Markdown/Test3_0.md" -J "Test3_0" -env MYARGS="-name Test3-0 -GPU False -time 3600 -b 2.0 -a 2 -d fd -ID 0" < submit_cpu.sh
