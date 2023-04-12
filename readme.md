# RSA


## Usage 
```
Generates public/private keys + encodes/decodes text

optional arguments:
  -m {generate,encrypt,decrypt}, --mode {generate,encrypt,decrypt}
                        Choose type of action
  -k KEY, --key KEY     keys for encoding/decoding
  -i INPUT, --input INPUT
                        input file
  -o OUTPUT, --output OUTPUT
                        output file
```
## Examples 

Generating keys
```
python3 main.py --mode generate
public key: 478660882692307931,40941800364181286149
private key: 11016910267299234899,40941800364181286149

```

Encrypting
```
python3 main.py --mode encrypt --key  478660882692307931,40941800364181286149 -i input -o output

```

Decrypting
```
python3 main.py --mode decrypt --key  11016910267299234899,40941800364181286149 --input output --output
 decrypt

```