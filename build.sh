#!/bin/bash

# Hardcoded configuration
sdk_version="8.3.4"  # Replace with the desired SDK version
root_dir="./"        # Root directory containing all projects
package="web"        # Hardcoded to only build for the web platform
include_steam_lib="false"  # Steam library inclusion is hardcoded to false

# Variables
sdk_name="renpy-${sdk_version}-sdk"

# Download and extract the SDK
echo "Downloading SDK: ${sdk_name}..."
wget -q https://www.renpy.org/dl/${sdk_version}/${sdk_name}.tar.bz2
tar -xf ${sdk_name}.tar.bz2
rm ${sdk_name}.tar.bz2
mv ${sdk_name} renpy

# Loop through project directories in the root directory
for project_dir in ${root_dir}/*; do
  if [ -d "${project_dir}" ] && [ -f "${project_dir}/game/script.rpy" ]; then
    echo "Building project: ${project_dir}"

    # Build the project for the web platform
    ./renpy/renpy.sh ./renpy/launcher distribute --package ${package} ${project_dir}

    # Check if the build succeeded
    if [ $? -eq 0 ]; then
      build_dir=$(find "${project_dir}" -name '*-dists' -type d | head -n 1)
      echo "Build completed for ${project_dir}. Output directory: ${build_dir}"
    else
      echo "Build failed for ${project_dir}."
      exit 1
    fi
  else
    echo "Skipping ${project_dir}: Not a valid Ren'Py project."
  fi
done

echo "All projects built successfully!"
