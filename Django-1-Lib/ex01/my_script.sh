#!/bin/sh

python3 -m pip --version
python3 -m pip install --force-reinstall --target=local_lib git+https://github.com/jaraco/path > pip.log 2>&1
if [ $? -eq 0 ]; then
    echo "Successfully installed"
    python3 my_program.py
else
    echo "Failed to install"
fi
