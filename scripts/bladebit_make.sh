#!/bin/env bash
#
# Installs bladebit - A fast RAM-only, k32-only, Chia plotter.
# 416 GiB of RAM are needed. See https://github.com/harold-b/bladebit
# NOTE: Bladebit checks proc count at build time, so must build when Docker first launched
#

if [[ ${mode} == 'fullnode' ]] || [[ ${mode} =~ ^plotter.* ]]; then
    if [ ! -f /usr/bin/bladebit ]; then
        cd /bladebit
        # Build the code, previously cloned when image was built on Github build servers
        arch_name="$(uname -m)"
        echo "arch_name=${arch_name}"
        if [ "${arch_name}" = "x86_64" ]; then
            echo "Building bladebit on x86_64..."
            mkdir -p build && cd build
            cmake ..
            cmake --build . --target bladebit --config Release
            mv ./bladebit /usr/bin/bladebit
            cd .. && rm -r ./build
            echo "Bladebit version: "`bladebit --version`
        elif [ "${arch_name}" = "arm64" ]; then
            echo "Building bladebit on arm64..."
            mkdir -p build && cd build
            cmake ..
            cmake --build . --target bladebit --config Release
            mv ./bladebit /usr/bin/bladebit
            cd .. && rm -r ./build
            echo "Bladebit version: "`bladebit --version`
        else
            echo "Building bladebit skipped -> unsupported architecture: ${arch_name}"
        fi
    fi
fi
