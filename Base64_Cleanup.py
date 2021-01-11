#!/usr/bin/python3
"""
This script is just to clean up Base64 if is has � present in the output. 

Example:
$�G�r�o�U�P�P�O�L�i�C�Y�S�E�t�t�I�N�G�s� �=� �[�r�E�F�]�.�A�S�s�e�M�B�L�Y�.�G�E�t�T�y�p�E�

$GroUPPOLiCYSEttINGs = [rEF].ASseMBLY.GEtTypE
"""

with open("./target.txt", "r") as f_obj:
    data = f_obj.read()
    cleaned = data.replace("�", "")
    print(cleaned)
