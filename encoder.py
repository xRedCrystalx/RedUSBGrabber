import sys, base64
sys.dont_write_bytecode = True

with open("main.pyw", "r", encoding="utf-8") as source_code_file:
    source_code: str = source_code_file.read()
    
source_code = base64.b64encode(source_code.encode(encoding="ascii")).decode("ascii")

full_code: str = f"""
import sys, base64
sys.dont_write_bytecode = True

kHJ3kjIhjk = "{source_code}"

jlpihi = "6b!sh(diec4od)x.'#fha"

eval(jlpihi[8]+jlpihi[14]+jlpihi[8]+jlpihi[9]+jlpihi[5]+jlpihi[1]+jlpihi[20]+jlpihi[3]+jlpihi[8]+jlpihi[0]+jlpihi[10]+jlpihi[15]+jlpihi[1]+jlpihi[0]+jlpihi[10]+jlpihi[12]+jlpihi[8]+jlpihi[9]+jlpihi[11]+jlpihi[12]+jlpihi[8]+jlpihi[5]+jlpihi[16]+kHJ3kjIhjk+jlpihi[16]+jlpihi[13]+jlpihi[15]+jlpihi[12]+jlpihi[8]+jlpihi[9]+jlpihi[11]+jlpihi[12]+jlpihi[8]+jlpihi[5]+jlpihi[16]+jlpihi[20]+jlpihi[3]+jlpihi[9]+jlpihi[7]+jlpihi[7]+jlpihi[16]+jlpihi[13]+jlpihi[13])

"""

with open(f"./results/enocded.pyw", "w", encoding="utf-8") as encoded_file:
    encoded_file.write(full_code)
