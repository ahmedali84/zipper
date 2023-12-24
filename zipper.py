import zipfile
import json
from pathlib import Path

JSON_CONFIG = "to_zip.json"

def import_json(filepath):
    """Return the content of a json filepath"""
    with open(filepath) as json_content:
        content = json_content.read()

    return json.loads(content)

def main():
    """
    Create a zip file in current directory using JSON_CONFIG file as a
    reference for the files/directories to include/exclude in the output
    zip file.
    """
    # read the paths list from the json file
    cwd = Path.cwd()
    to_zip = import_json(cwd / JSON_CONFIG)
    paths_to_zip = []

    # if ignore == True exclude the paths list in json from being zipped 
    # and zip everything else
    if to_zip['ignore']:
       for path in cwd.iterdir():
           if path.name not in to_zip['paths']:
               if path.is_dir():
                   paths_to_zip.extend(list(path.rglob("*")))

               if path.is_file():
                   paths_to_zip.append(path)

    # ignore == False
    # zip only the paths included in the json paths list
    else:
        for name in to_zip['paths']:
            path = cwd / name
            if path.is_dir():
                paths_to_zip.extend(list(path.rglob("*")))
            
            if path.is_file():
                paths_to_zip.append(path)

    # filter out non existing files
    paths_to_zip = [path for path in paths_to_zip if path.exists()]

    # filter out existing zip file and script relevant files.
    exclude_paths = [
        JSON_CONFIG, 
        Path(__file__).name, 
        to_zip['zip']
    ]
    paths_to_zip = [
        path for path in paths_to_zip if path.name not in exclude_paths
    ]

    # zip all the files in the list
    with zipfile.ZipFile(to_zip['zip'], 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in paths_to_zip:
            print(f"Adding: {path.relative_to(cwd)}")
            archive.write(
                path, 
                # this line will create a subfolder in the archive
                # that has the same name of the zip file with the ".zip" stripped
                arcname=f"{to_zip['zip'].replace('.zip', '')}/{path.relative_to(cwd)}"
            )

    # confirm zip file creation
    zip_file = cwd / to_zip['zip']
    if zip_file.exists():
        print(f"Created successfully: {zip_file}")
        
def test():
    print(Path(__file__))

if __name__ == '__main__':
    main()
    # test()