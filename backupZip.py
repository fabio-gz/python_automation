"""
Backing up a folder into a zip file
"""

import zipfile
import os


def backupToZip(folder):
    folder = os.path.abspath(folder)  # absolute path

    number = 1

    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'

        if not os.path.exists(zipFilename):
            break
        number = number + 1

        print(f'Creaating {zipFilename}')

        backupzip = zipfile.ZipFile(zipFilename, 'w')

        for foldername, _, filenames in os.walk(folder):
            print(f'Adding files in {foldername}')
            backupzip.write(foldername)

            for filename in filenames:
                newBase = os.path.basename(folder) + '_'
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue
                backupzip.write(os.path.join(foldername, filename))
        backupzip.close()

        print('Done')
