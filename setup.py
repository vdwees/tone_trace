from setuptools import setup, find_packages

setup(
    name="tone_trace",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=["simpleaudio==1.0.2"],
    entry_points={"console_scripts": ["tone_trace = tone_trace.tone_trace:main"]},
)

