# RedUSBGrabber
Pen testing tool for USB copying attack.

## Instalation
As any other github repos

```bash
git clone https://github.com/xRedCrystalx/RedUSBGrabber
cd RedUSBGrabber/
```

## Usage

`main.py` is the actual script that runs the malicious code. Executing the file will result as a background task and can be safely terminated using `TaskManager` or any other process/task killing software.
```java
python3 main.py     // Linux/MacOS
py main.py          // Windows 
```

You can also use `encoder.py`, this will hide the sorce code under the base64 encoding, a layer for bypassing some anti-virus solutions. Encoded file will be saved in `./results/` folder.
```java
python3 encoder.py  // Linux/MacOS
py encoder.py       // Windows 
```

## Disclamer

This USB copying attack script is intended for educational and research purposes only. It is designed to demonstrate potential vulnerabilities in systems and raise awareness about security risks associated with USB devices.

By using this script, you acknowledge that you understand the risks involved and agree to use it responsibly and ethically. You must obtain proper authorization before conducting any testing on systems that you do not own or have explicit permission to test.

The creator of this script cannot be held responsible for any damages, legal consequences, or misuse resulting from the use of this tool. It is your responsibility to ensure compliance with all applicable laws and regulations.

Furthermore, this script should not be used to access, modify, or distribute any data or information without proper authorization. Unauthorized access to systems or data is illegal and unethical.

Remember, the primary purpose of pen testing tools like this one is to improve security by identifying and addressing vulnerabilities. Misuse of these tools can have serious consequences. Use it responsibly and with caution.

By using this script, you agree to the terms outlined in this disclaimer. If you do not agree with these terms, do not use the script.