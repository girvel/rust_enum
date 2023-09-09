import setuptools

setuptools.setup(
  name="rust_enum",
  version="1.0.0",
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
)
