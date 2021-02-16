# Project template

## Project structure

```
.
├── notebooks
│   └── 01_sample_notebook.ipynb
├── project
│   ├── main.py
│   ├── sub1
│   │   ├── __init__.py
│   │   └── helper.py
│   ├── sub2
│   │   ├── __init__.py
│   │   └── utils.py
│   └── tests
│       ├── __init__.py
│       ├── test_main.py
│       ├── test_sub1.py
│       └── test_sub2.py
├── README.md
└── setup.py
```

## Notes:

### Run test

```
pytest
```

## Resources

- Notebook import: https://stackoverflow.com/questions/34478398/import-local-function-from-a-module-housed-in-another-directory-with-relative-im
- Minimal setup.py : https://github.com/maet3608/minimal-setup-py/blob/master/setup.py
- Project directory structure: https://gaopinghuang0.github.io/2018/08/03/python3-import-and-project-layout
- Project directory structure: https://gist.github.com/tasdikrahman/2bdb3fb31136a3768fac
- Project template: https://sourcery.ai/blog/python-best-practices/
- GitHub Action: https://wkrzywiec.medium.com/how-to-write-good-quality-python-code-with-github-actions-2f635a2ab09a
- Some more stuff related to GitHub actions: https://wemake-python-stylegui.de/en/latest/pages/usage/integrations/github-actions.html

* `__main__`: https://www.geeksforgeeks.org/usage-of-__main__-py-in-python/
