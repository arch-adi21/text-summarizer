import setuptools

with open("README.md", "r" , encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.0"
REPO_NAME = "text-summarizer"
AUTHOR_USER_NAME = "arch-adi21"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "22f3001792@ds.study.iitm.ac.in"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls= {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        "Source Code": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")
)