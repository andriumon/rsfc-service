def make_github_raw_url(indicator_name: str) -> str:
    return (
        f"https://raw.githubusercontent.com/EVERSE-ResearchSoftware/indicators/main/indicators/{indicator_name}.json"
    )