#!/bin/sh
mkdir -p outputs/Example1/Markdown
bsub -o "outputs/Example1/Markdown/Example1_0.md" -J "Example1_0" -env MYARGS="-name Example1-0 -GPU False -time 3600 -b 4.0 -a 1 -d dsf -k <relive.P1 object at 0x00000142599387F0> -ID 0" < submit_cpu.sh
mkdir -p outputs/Example2/Markdown
bsub -o "outputs/Example2/Markdown/Example2_0.md" -J "Example2_0" -env MYARGS="-name Example2-0 -GPU True -time 3600 -b 4.0 -a 1 -d dssf -k <relive.P1 object at 0x00000142599387F0> -ID 0" < submit_gpu.sh
mkdir -p outputs/Example3/Markdown
bsub -o "outputs/Example3/Markdown/Example3_0.md" -J "Example3_0" -env MYARGS="-name Example3-0 -GPU False -time 3600 -b 2.0 -a 2 -d fd -k <relive.P1 object at 0x0000014259904370> -ID 0" < submit_cpu.sh
bsub -o "outputs/Example3/Markdown/Example3_1.md" -J "Example3_1" -env MYARGS="-name Example3-1 -GPU False -time 3600 -b 2.0 -a 2 -d fd -k <relive.P1 object at 0x0000014259904370> -ID 1" < submit_cpu.sh
