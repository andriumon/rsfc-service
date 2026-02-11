import subprocess
from app.data import utils
import tempfile
import os
import json


async def pull_docker_image():

    print("Pulling RSFC Docker image")
    
    subprocess.run(
        ["docker", "pull", utils.RSFC_DOCKER_IMAGE],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    print("Image pulled succesfully")


async def run_assessment(resource_identifier, test_id, github_token):
    
    print("Running RSFC container")
    
    tempdir = tempfile.mkdtemp()

    try:

        cmd = [
            "docker",
            "run",
            "--rm",
            "-v", f"{tempdir}:/rsfc/rsfc_output",
            utils.RSFC_DOCKER_IMAGE,
            "--repo",
            resource_identifier,
            "--ftr"
        ]
        
        if test_id is not None:
            cmd.extend(["--id", test_id])
            
        cmd.extend(["-t", github_token])

        subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        files = os.listdir(tempdir)

        report_filename = "rsfc_assessment.json"
        if report_filename not in files:
            raise RuntimeError(
                f"{report_filename} not found in RSFC output directory. "
                f"Files generated: {files}"
            )

        report_path = os.path.join(tempdir, report_filename)
        
        with open(report_path) as f:
            report = json.load(f)
        
        return report

    except Exception as e:
        raise Exception(f"Error while running the container: {e}")

