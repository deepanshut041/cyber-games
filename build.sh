#!/bin/bash

# Hardcoded configuration
sdk_version="8.3.4"  # Replace with the desired SDK version
root_dir="./"        # Root directory containing all projects
package="web"        # Hardcoded to only build for the web platform
include_steam_lib="false"  # Steam library inclusion is hardcoded to false

# Variables
sdk_name="renpy-${sdk_version}-sdk"
output_dir="gh-pages"  # Directory to store unzipped outputs for deployment
web_tools="renpy-${sdk_version}-web"

# Download and extract the SDK
echo "Downloading SDK: ${sdk_name}..."
wget -q https://www.renpy.org/dl/${sdk_version}/${sdk_name}.tar.bz2
tar -xf ${sdk_name}.tar.bz2
rm ${sdk_name}.tar.bz2
mv ${sdk_name} renpy

# Download Web Build Support
echo "Downloading Web Build Support..."
wget -q https://www.renpy.org/dl/${sdk_version}/${web_tools}.zip
unzip -q "${web_tools}.zip" -d renpy
rm "${web_tools}.zip"


# Loop through project directories in the root directory
for project_dir in ${root_dir}/*; do
  if [ -d "${project_dir}" ] && [ -f "${project_dir}/game/script.rpy" ]; then
    echo "Building project: ${project_dir}"
    project_name=$(basename "${project_dir}")

    # Build the project for the web platform
    ./renpy/renpy.sh ./renpy/launcher web_build ${project_dir}

    # Check if the build succeeded
    if [ $? -eq 0 ]; then
      build_dir=$(find "${root_dir}" -type d -name '*-dists' | head -n 1)
      if [ -d "${build_dir}" ]; then
        game_dir=$(find "${build_dir}" -type d -name '*-web' | head -n 1)
        if [ -d "${game_dir}" ]; then
          mv ${game_dir}  "${output_dir}/${project_name}"

          rm -rf "${build_dir}"
          echo "Removed build directory: ${build_dir}"
        else
          echo "No build directory found for ${project_name}."
        fi
      else
        echo "No build directory found for ${project_name}."
      fi
    else
      echo "Build failed for ${project_name}."
      exit 1
    fi
  else
    echo "Skipping ${project_dir}: Not a valid Ren'Py project."
  fi
done

echo "All projects built and extracted successfully! Outputs are in ${output_dir}."
