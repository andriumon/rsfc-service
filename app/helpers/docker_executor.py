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


async def run_assessment(resource_identifier, test_id):
    
    github_token = None
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "../config.json")

    if os.path.isfile(config_path):
        try:
            with open(config_path) as f:
                config = json.load(f)
                github_token = config.get("github_token")
        except Exception as e:
            print(f"Warning: could not read config.json ({e}), proceeding without github token")
    
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
            
        if github_token:
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

