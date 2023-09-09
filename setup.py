from pathlib import Path

import setuptools

setuptools.setup(
  name="rust_enum",
  version="1.0.1",
  author="Nikita Girvel Dobrynin",
  author_email="widauka@ya.ru",
  description="Rust-style enums",
  url="https://github.com/girvel/rust_enum",
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  package_dir={"": "."},
  packages=["."],
  python_requires=">=3.6",
  long_description=(Path(__file__).parent / "README.md").read_text(),
  long_description_content_type='text/markdown',
)
