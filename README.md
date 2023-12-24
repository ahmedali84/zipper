# Zipper
Zipper is a python script to automatically zip specific files in my repo whenever I need to send them for testing, As a Blender coder I needed to zip my addons by manually picking up the relevant addon files (excluding git files) which was a waste of time and prune to mistakes.
This script parses the content of `to_zip.json` file, the parameters in this file are:
- `zip` : the name of the output zip file.
- `ignore`: a boolean value to decide whether to exclude the filenames saved in `paths` (`ignore = true`), or to include them exclusively in the output zip file (`ignore = false`).
- `paths`: a list of filenames in the current directory to be included or excluded in/from the output zip file.
### Example
```json
{
    "zip": "output.zip", 
    "ignore": true, 
    "paths": [
        ".gitignore", 
        ".git", 
        "README.md", 
        "folder_to_ignore"
    ]
}
```
### Notes
- The script already excludes the script and the json files from the output zip file content, it also exludes any old versions of the zip file.
- You may want to exclude the above files in your `.gitignore` file as well.