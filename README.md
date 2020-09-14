# code2markdown
Exports all source code of a directory to a markdown file. Adds a filetree as well.

## Ẁhat can it do?
Export the contents of a files in a dir to markdown code blocks.
This can be used for example as a helper for written assignments when the
contents need to be included as a text export.

## Install
1. Download this project.
2. Install dependencies: `pip install -r requirements.txt`

## Usage
```sh
python ./code_export.py /path/to/my/project/
```

## Create a file tree
A tree of the directory is also prepended.

## Ignore files and dirs
Files and dirs can also be ignore via gitignore style patterns provided in
a `patterns.list` file. (Note that pattern might not affect the tree creation.)
