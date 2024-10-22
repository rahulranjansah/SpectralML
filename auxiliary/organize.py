import hashlib
import os
import pathlib
import tarfile
import urllib.request


# defining a function to compute the sha256 value of the downloaded files

def comp_sha256(file_name):
    """
    Compute the SHA256 hash of a file.
    Parameters
    ----------
    file_name : str
    Absolute or relative pathname of the file that shall be parsed.
    Returns
    -------
    sha256_res : str
    Resulting SHA256 hash.
    """

    # Set the SHA356 hashing
    hash_sha256 = hashlib.sha256()

    # Open the file in binary mode (read-only) and parse it in bytechunks 65,536 (
    # in case of large files, the loading will not exceed the usable RAM)

    with pathlib.Path(file_name).open(mode="rb") as f_temp:
        for _seq in iter(lambda: f_temp.read(65536), b""):
            hash_sha256.update(_seq)

    # disgest the SHA256 result
    sha256_res = hash_sha256.hexdigest()

    return sha256_res


def download_file(dl_path, dl_url):
    """
    download_file(dl_path, dl_url)

    This helper function supports one to download files from the Internet and
    stores them in a local directory.

    Parameters
    ----------
    dl_path : str
        Download path on the local machine, relative to this function.
    dl_url : str
        Download url of the requested file.
    """

    # Obtain the file name from the url string. The url is split at
    # the "/", thus the very last entry of the resulting list is the file's
    # name
    file_name = dl_url.split('/')[-1]

    # Create necessary sub-directories in the DL_PATH direction (if not
    # existing)
    pathlib.Path(dl_path).mkdir(parents=True, exist_ok=True)

    # If the file is not present in the download directory -> download it
    if not os.path.isfile(dl_path + file_name):

        # Download the file with the urllib  package
        urllib.request.urlretrieve(dl_url, dl_path + file_name)

#
