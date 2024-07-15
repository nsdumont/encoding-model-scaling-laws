import os
import subprocess
import cortex

pycortex_download_script = "../ds003020-2.2.0.sh"
pycortex_dir = '../pycortex-db'

# Select which subjects to download (full list is ['UTS01', 'UTS02','UTS03','UTS04','UTS05','UTS06','UTS07','UTS08'] ) 
subjects = ['UTS01', 'UTS02','UTS03']

with open(pycortex_download_script, 'r') as f:
    for line in f:
        if 'derivative/pycortex-db/UTS' in line:
            for subject in subjects:
                if subject in line:
                    # Construct the output command
                    output_command = line.replace(' derivative/pycortex-db/', ' ' + pycortex_dir + os.sep)
                    
                    # Extract the output file path from the curl command
                    # Assuming the output path is specified with -o option in the curl command
                    parts = output_command.split()
                    output_file_path = None
                    if '-o' in parts:
                        output_file_index = parts.index('-o') + 1
                        output_file_path = parts[output_file_index]
                    
                    # Check if the file exists
                    if output_file_path and not os.path.exists(output_file_path):
                        subprocess.run(output_command, shell=True)
                    else:
                        print(f"File {output_file_path} already exists. Skipping download.")

# This is your new filestore path
new_filestore_path = os.path.join(os.getcwd(), pycortex_dir)
# Set the new filestore path
cortex.utils.config.set('basic', 'filestore', new_filestore_path)
# Optionally, print the current configuration to verify the change
print("Current filestore path:", cortex.utils.config.get('basic', 'filestore'))