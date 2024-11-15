import os
import hashlib

def check_sha256(file_path, expected_hash):
    """
    Check the SHA256 hash of a file against an expected hash.
    
    :param file_path: Path to the file to check
    :param expected_hash: The expected SHA256 hash
    :return: True if the hash matches, False otherwise
    """
    sha256_hash = hashlib.sha256()
    
    # Open the file and compute its hash
    with open(file_path, "rb") as f:
        # Read the file in chunks to avoid memory overload for large files
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    
    # Compare computed hash with expected hash
    return sha256_hash.hexdigest() == expected_hash

def verify_files_in_folder(folder_path, sums_file_path, report_file_path):
    """
    Verify the SHA256 checksums for all files in a folder based on the SHA256SUMS file
    and write the passed checks to a report file.
    
    :param folder_path: Path to the folder containing the files
    :param sums_file_path: Path to the SHA256SUMS file
    :param report_file_path: Path to the output report file
    """
    # Read the SHA256SUMS file and store the expected hash values
    expected_hashes = {}
    with open(sums_file_path, 'r') as sums_file:
        for line in sums_file:
            # Skip empty lines or comments
            if line.strip() and not line.startswith('#'):
                expected_hash, file_name = line.split()
                expected_hashes[file_name] = expected_hash

    # Open the report file for writing the results
    with open(report_file_path, 'w') as report_file:
        # Iterate through the files in the folder and check their SHA256 hash
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            # Skip directories and process only files
            if os.path.isfile(file_path):
                # Check if this file is listed in the SHA256SUMS file
                if file_name in expected_hashes:
                    expected_hash = expected_hashes[file_name]
                    if check_sha256(file_path, expected_hash):
                        report_file.write(f"{file_name}: SHA256 check passed.\n")
                    else:
                        report_file.write(f"{file_name}: SHA256 check failed.\n")
                else:
                    report_file.write(f"{file_name}: Not listed in SHA256SUMS file.\n")
                    
    print(f"Report saved to {report_file_path}")

# Usage
folder_path = "data"  # Path to the folder containing the files
sums_file_path = "data\\SHA256SUMS.txt"  # Path to the SHA256SUMS file
report_file_path = "data_checksum_report.txt"  # Path to save the report
verify_files_in_folder(folder_path, sums_file_path, report_file_path)


